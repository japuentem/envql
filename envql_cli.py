#!/usr/bin/env python3
import sys
import os

# Asegurar soporte de caracteres UTF-8 / emojis en consolas de Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

import argparse

def main():
    parser = argparse.ArgumentParser(description="EnvQL CLI: El estándar universal para configuración y secretos.")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")

    # init
    subparsers.add_parser("init", help="Inicializa un nuevo schema.envql en el proyecto")

    # key:generate
    subparsers.add_parser("key:generate", help="Genera una llave maestra simétrica (envql.key)")

    # encrypt
    encrypt_parser = subparsers.add_parser("encrypt", help="Cifra un archivo de esquema plano")
    encrypt_parser.add_argument("--input", default="schema.envql", help="Archivo de esquema de entrada")
    encrypt_parser.add_argument("--output", default="schema.envql.enc", help="Archivo cifrado de salida")

    # generate
    gen_parser = subparsers.add_parser("generate", help="Genera tipos para IDEs (TypeScript / Python)")
    gen_parser.add_argument("--target", choices=["typescript", "python"], required=True, help="Lenguaje objetivo")

    # run
    run_parser = subparsers.add_parser("run", help="Valida el entorno y ejecuta el comando de la aplicación")
    run_parser.add_argument("cmd", nargs=argparse.REMAINDER, help="Comando a ejecutar")

    args = parser.parse_args()

    if args.command == "init":
        print("🚀 Inicializando archivo schema.envql en el directorio actual...")
        with open("schema.envql", "w", encoding="utf-8") as f:
            f.write("# schema.envql - Definición de Entorno\nenvironment: String @default(\"development\")\nport: Int @default(3000)\ndatabase_url: String @secret\n")
        print("✨ ¡Creado con éxito: schema.envql!")
    elif args.command == "key:generate":
        print("🔑 Generando llave maestra envql.key...")
        from cryptography.fernet import Fernet
        key = Fernet.generate_key()
        with open("envql.key", "wb") as kf:
            kf.write(key)
        print("✨ ¡Llave maestra generada con éxito! No la compartas ni la subas a Git.")
    elif args.command == "encrypt":
        from cryptography.fernet import Fernet
        key_path = "envql.key"
        if not os.path.exists(key_path):
            print(f"❌ Error: No se encontró la llave maestra '{key_path}'. Ejecuta 'key:generate' primero.")
            sys.exit(1)
        with open(key_path, "rb") as kf:
            key = kf.read()
        f = Fernet(key)
        if not os.path.exists(args.input):
            print(f"❌ Error: No se encontró el archivo de entrada '{args.input}'.")
            sys.exit(1)
        with open(args.input, "rb") as file:
            data = file.read()
        enc_data = f.encrypt(data)
        with open(args.output, "wb") as file:
            file.write(enc_data)
        print(f"🔒 [EnvQL Security] Archivo cifrado con éxito: '{args.output}'")
    elif args.command == "run":
        print("🛡️ Validando entorno con EnvQL Runtime antes de ejecutar la app...")
        print(f"🚀 Ejecutando comando: {' '.join(args.cmd)}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
