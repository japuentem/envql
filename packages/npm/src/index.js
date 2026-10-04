const crypto = require('crypto');
const fs = require('fs');
const path = require('path');

class EnvQLError extends Error {
  constructor(message) {
    super(message);
    this.name = 'EnvQLError';
  }
}

/**
 * Fernet Spec (AES-128-CBC + HMAC-SHA256, total 256 bits key urlsafe-base64)
 * 32 bytes key: first 16 bytes = signing key (HMAC), second 16 bytes = encryption key (AES)
 */
function parseFernetKey(keyBase64) {
  const rawKey = Buffer.from(keyBase64.trim(), 'base64');
  if (rawKey.length !== 32) {
    throw new EnvQLError('❌ La llave Fernet maestra debe tener exactamente 32 bytes decodificados.');
  }
  const signingKey = rawKey.subarray(0, 16);
  const encryptionKey = rawKey.subarray(16, 32);
  return { signingKey, encryptionKey };
}

function decryptFernet(tokenBase64, keyBase64) {
  const { signingKey, encryptionKey } = parseFernetKey(keyBase64);
  const token = Buffer.from(tokenBase64.trim(), 'base64');

  if (token.length < 73) {
    throw new EnvQLError('❌ Token Fernet corrupto o longitud insuficiente.');
  }

  const version = token[0];
  if (version !== 0x80) {
    throw new EnvQLError(`❌ Versión Fernet no soportada: 0x${version.toString(16)}`);
  }

  // Verificar HMAC (los últimos 32 bytes son el HMAC-SHA256)
  const dataToSign = token.subarray(0, token.length - 32);
  const hmacReceived = token.subarray(token.length - 32);

  const hmacComputed = crypto.createHmac('sha256', signingKey).update(dataToSign).digest();
  if (!crypto.timingSafeEqual(hmacReceived, hmacComputed)) {
    throw new EnvQLError('❌ Firma HMAC Fernet inválida: llave maestra incorrecta o archivo alterado.');
  }

  // IV = bytes 9 a 25 (16 bytes)
  const iv = token.subarray(9, 25);
  // Ciphertext = bytes 25 hasta (longitud - 32)
  const ciphertext = token.subarray(25, token.length - 32);

  const decipher = crypto.createDecipheriv('aes-128-cbc', encryptionKey, iv);
  let decrypted = decipher.update(ciphertext);
  decrypted = Buffer.concat([decrypted, decipher.final()]);

  return decrypted.toString('utf-8');
}

function encryptFernet(plainText, keyBase64) {
  const { signingKey, encryptionKey } = parseFernetKey(keyBase64);
  const version = Buffer.from([0x80]);

  // Timestamp 64-bit big endian
  const timestamp = Buffer.alloc(8);
  const nowSeconds = BigInt(Math.floor(Date.now() / 1000));
  timestamp.writeBigUInt64BE(nowSeconds, 0);

  // IV 16 bytes aleatorios
  const iv = crypto.randomBytes(16);

  const cipher = crypto.createCipheriv('aes-128-cbc', encryptionKey, iv);
  const data = Buffer.from(plainText, 'utf-8');
  let ciphertext = cipher.update(data);
  ciphertext = Buffer.concat([ciphertext, cipher.final()]);

  const basicParts = Buffer.concat([version, timestamp, iv, ciphertext]);
  const hmac = crypto.createHmac('sha256', signingKey).update(basicParts).digest();

  const token = Buffer.concat([basicParts, hmac]);
  return token.toString('base64');
}

function generateMasterKey(keyPath = 'envql.key') {
  const key = crypto.randomBytes(32).toString('base64');
  fs.writeFileSync(keyPath, key, { encoding: 'utf-8' });
  console.log(`🔑 [EnvQL Security] Llave maestra generada en '${keyPath}'. ¡No la subas a Git!`);
  return key;
}

function loadMasterKey(keyPath = 'envql.key') {
  if (process.env.ENVQL_MASTER_KEY) {
    return process.env.ENVQL_MASTER_KEY.trim();
  }
  if (!fs.existsSync(keyPath)) {
    throw new EnvQLError(`❌ No se encontró la llave maestra en '${keyPath}' ni en ENVQL_MASTER_KEY.`);
  }
  return fs.readFileSync(keyPath, 'utf-8').trim();
}

function parseSchemaLine(line) {
  const clean = line.trim();
  if (!clean || clean.startsWith('#')) return null;

  const colonIdx = clean.indexOf(':');
  if (colonIdx === -1) return null;

  const key = clean.substring(0, colonIdx).trim();
  const rest = clean.substring(colonIdx + 1).trim();

  const modParts = rest.split('@');
  const varType = modParts[0].trim();

  const modifiers = {};
  for (let i = 1; i < modParts.length; i++) {
    const mod = modParts[i].trim();
    if (mod.startsWith('default(')) {
      const valStr = mod.substring(8, mod.lastIndexOf(')')).trim().replace(/^["']|["']$/g, '');
      modifiers.default = valStr;
    } else if (mod === 'secret') {
      modifiers.secret = true;
    }
  }

  return { key, type: varType, modifiers };
}

function load(options = {}) {
  const schemaEncPath = options.schemaPath || 'schema.envql.enc';
  const keyPath = options.keyPath || 'envql.key';

  const masterKey = loadMasterKey(keyPath);

  if (!fs.existsSync(schemaEncPath)) {
    throw new EnvQLError(`❌ No se encontró el esquema cifrado: '${schemaEncPath}'.`);
  }

  const encryptedContent = fs.readFileSync(schemaEncPath, 'utf-8');
  const decryptedSchema = decryptFernet(encryptedContent, masterKey);
  const lines = decryptedSchema.split(/\r?\n/);

  const config = {};

  lines.forEach((line, idx) => {
    const parsed = parseSchemaLine(line);
    if (!parsed) return;

    const { key, type, modifiers } = parsed;
    const envKey = key.toUpperCase();
    let rawVal = process.env[envKey];

    if (rawVal === undefined || rawVal === '') {
      if ('default' in modifiers) {
        rawVal = modifiers.default;
      } else {
        throw new EnvQLError(`❌ Línea ${idx + 1}: La variable obligatoria '${envKey}' no está definida.`);
      }
    }

    // Cast estricto con validación Fail-Fast
    if (type === 'Int') {
      const num = parseInt(rawVal, 10);
      if (isNaN(num)) {
        throw new EnvQLError(`❌ Línea ${idx + 1}: '${envKey}' debe ser de tipo Int. Valor recibido: '${rawVal}'.`);
      }
      config[key] = num;
    } else if (type === 'Boolean') {
      const lower = String(rawVal).toLowerCase();
      if (['true', '1', 'yes', 'on'].includes(lower)) {
        config[key] = true;
      } else if (['false', '0', 'no', 'off'].includes(lower)) {
        config[key] = false;
      } else {
        throw new EnvQLError(`❌ Línea ${idx + 1}: '${envKey}' debe ser Boolean. Valor recibido: '${rawVal}'.`);
      }
    } else {
      config[key] = String(rawVal);
    }
  });

  return config;
}

module.exports = {
  load,
  decryptFernet,
  encryptFernet,
  generateMasterKey,
  loadMasterKey,
  parseSchemaLine,
  EnvQLError
};
