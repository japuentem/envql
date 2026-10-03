import os
import sys

# Asegurar soporte de caracteres UTF-8 / emojis en consolas de Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from cryptography.fernet import Fernet

class EnvQLError(Exception):
    pass

# --- MÓDULO DE CIFRADO (SECURITY LAYER) ---

def generate_master_key(key_path="envql.key"):
    """Genera una llave maestra simétrica para cifrar/descifrar configuraciones."""
    key = Fernet.generate_key()
    with open(key_path, "wb") as key_file:
        key_file.write(key)
    print(f"🔑 [EnvQL Security] Llave maestra generada y guardada en '{key_path}'. ¡No la subas a Git!")

def load_master_key(key_path="envql.key"):
    """Carga la llave maestra desde el disco o desde variables del sistema."""
    env_key = os.getenv("ENVQL_MASTER_KEY")
    if env_key:
        return env_key.encode()
        
    if not os.path.exists(key_path):
        raise EnvQLError(f"❌ No se encontró la llave maestra en '{key_path}' ni en ENVQL_MASTER_KEY.")
        
    with open(key_path, "rb") as key_file:
        return key_file.read()

def encrypt_schema(plain_schema_path, encrypted_output_path="schema.envql.enc", key_path="envql.key"):
    """Cifra un archivo de esquema plano para que sea seguro almacenarlo en Git."""
    key = load_master_key(key_path)
    f = Fernet(key)
    
    with open(plain_schema_path, "rb") as file:
        file_data = file.read()
        
    encrypted_data = f.encrypt(file_data)
    
    with open(encrypted_output_path, "wb") as file:
        file.write(encrypted_data)
        
    print(f"🔒 [EnvQL Security] Archivo cifrado con éxito: '{encrypted_output_path}'")

def decrypt_and_read_schema(encrypted_schema_path="schema.envql.enc", key_path="envql.key"):
    """Descifra el esquema en memoria de forma segura en tiempo de ejecución."""
    key = load_master_key(key_path)
    f = Fernet(key)
    
    if not os.path.exists(encrypted_schema_path):
        raise EnvQLError(f"❌ No se encontró el archivo cifrado: {encrypted_schema_path}")
        
    with open(encrypted_schema_path, "rb") as file:
        encrypted_data = file.read()
        
    try:
        decrypted_data = f.decrypt(encrypted_data)
        return decrypted_data.decode("utf-8").splitlines()
    except Exception as e:
        raise EnvQLError(f"❌ Error al descifrar el esquema. Llave incorrecta o archivo corrupto: {e}")

# --- PARSER Y RUNTIME ---

def parse_schema_line(line):
    line = line.strip()
    if not line or line.startswith("#"):
        return None
    
    parts = line.split(":")
    if len(parts) != 2:
        return None
    
    key = parts[0].strip()
    rest = parts[1].strip()
    mod_parts = rest.split("@")
    var_type = mod_parts[0].strip()
    
    modifiers = {}
    for mod in mod_parts[1:]:
        mod = mod.strip()
        if "default" in mod:
            val_str = mod.split("(")[1].rstrip(")").strip().strip('"').strip("'")
            modifiers["default"] = val_str
        elif "secret" in mod:
            modifiers["secret"] = True
            
    return {"key": key, "type": var_type, "modifiers": modifiers}

def validate_and_load_secure(encrypted_schema_path="schema.envql.enc"):
    """Descifra, valida y carga el entorno de forma segura."""
    print(f"🛡️ [EnvQL Runtime] Cargando esquema seguro cifrado desde '{encrypted_schema_path}'...")
    lines = decrypt_and_read_schema(encrypted_schema_path)
    
    config = {}
    for line_num, line in enumerate(lines, 1):
        parsed = parse_schema_line(line)
        if not parsed:
            continue
            
        key = parsed["key"]
        vtype = parsed["type"]
        mods = parsed["modifiers"]
        
        env_key = key.upper()
        raw_val = os.getenv(env_key)
        
        if raw_val is None:
            if "default" in mods:
                raw_val = mods["default"]
            else:
                raise EnvQLError(f"❌ Línea {line_num}: La variable obligatoria '{env_key}' no está definida.")
                
        # Tipado estricto
        if vtype == "Int":
            config[key] = int(raw_val)
        elif vtype == "Boolean":
            config[key] = str(raw_val).lower() in ("true", "1", "yes", "on")
        else:
            config[key] = str(raw_val)
            
    return config

if __name__ == "__main__":
    try:
        plain_file = "schema.envql"
        with open(plain_file, "w", encoding="utf-8") as f:
            f.write("environment: String @default(\"production\")\n")
            f.write("port: Int @default(8080)\n")
            f.write("database_url: String @secret\n")

        generate_master_key("envql.key")
        encrypt_schema(plain_file, "schema.envql.enc", "envql.key")

        os.environ["DATABASE_URL"] = "postgres://secure_user:super_secret_pass@db.internal:5432/prod_db"

        app_config = validate_and_load_secure("schema.envql.enc")

        print("\n🎉 ¡Entorno seguro cargado y validado exitosamente!")
        for k, v in app_config.items():
            display_v = "********" if k == "database_url" else v
            print(f"   • {k} = {display_v}")

    except EnvQLError as e:
        print(f"\n{e}")
        sys.exit(1)
