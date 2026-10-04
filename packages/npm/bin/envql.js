#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');
const { load, generateMasterKey, loadMasterKey, encryptFernet, EnvQLError } = require('../src/index');

const args = process.argv.slice(2);
const command = args[0];

function printHelp() {
  console.log(`
EnvQL CLI (Node.js & NPM Native)
El estándar universal para configuración y secretos.

Comandos disponibles:
  init             Inicializa un archivo schema.envql de ejemplo
  key:generate     Genera una llave maestra simétrica (envql.key)
  encrypt          Cifra schema.envql en schema.envql.enc
  run <comando>    Valida el entorno antes de ejecutar la aplicación
`);
}

switch (command) {
  case 'init':
    console.log('🚀 [EnvQL NPM] Inicializando schema.envql...');
    fs.writeFileSync(
      'schema.envql',
      '# schema.envql - Definición de Entorno\nenvironment: String @default("development")\nport: Int @default(3000)\ndatabase_url: String @secret\n',
      'utf-8'
    );
    console.log('✨ ¡Creado con éxito: schema.envql!');
    break;

  case 'key:generate':
    generateMasterKey('envql.key');
    break;

  case 'encrypt': {
    const key = loadMasterKey('envql.key');
    if (!fs.existsSync('schema.envql')) {
      console.error('❌ Error: No se encontró schema.envql');
      process.exit(1);
    }
    const plain = fs.readFileSync('schema.envql', 'utf-8');
    const encrypted = encryptFernet(plain, key);
    fs.writeFileSync('schema.envql.enc', encrypted, 'utf-8');
    console.log("🔒 [EnvQL Security] Archivo cifrado con éxito: 'schema.envql.enc'");
    break;
  }

  case 'run': {
    const subCmd = args.slice(1);
    if (subCmd.length === 0) {
      console.error("❌ Error: Debes especificar el comando. Ejemplo: npx envql run node src/server.js");
      process.exit(1);
    }
    console.log('🛡️ [EnvQL Runtime] Validando entorno con esquema cifrado...');
    let config;
    try {
      config = load({ schemaPath: 'schema.envql.enc', keyPath: 'envql.key' });
    } catch (err) {
      console.error(err.message);
      console.error('🚫 Abortando ejecución debido a fallo en validación de entorno.');
      process.exit(1);
    }

    const childEnv = { ...process.env };
    for (const [k, v] of Object.entries(config)) {
      childEnv[k.toUpperCase()] = String(v);
    }

    const child = spawn(subCmd[0], subCmd.slice(1), {
      stdio: 'inherit',
      env: childEnv,
      shell: true
    });

    child.on('exit', (code) => {
      process.exit(code || 0);
    });
    break;
  }

  default:
    printHelp();
    break;
}
