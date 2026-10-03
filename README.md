# EnvQL 🚀

> El estándar universal y multiplataforma para tipar, auditar y propagar configuración y secretos de forma segura.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Security: AES-256](https://img.shields.io/badge/security-AES--256-green.svg)](https://github.com/your-username/envql)

---

## 🔍 ¿Qué es EnvQL?

La configuración basada en archivos `.env` planos y ciegos es un estándar arcaico que provoca caídas en producción por un simple *typo* (`DATABASE_URLL`), fugas accidentales de credenciales en Git e inconsistencias entre lenguajes.

**EnvQL** introduce un lenguaje declarativo unificado para definir contratos estrictos de configuración y secretos. Funciona de manera similar a cómo GraphQL unificó las consultas o JSON el intercambio de datos.

---

## ✨ Características Principales

* **🛡️ Tipado Estricto y Validación (Fail-Fast):** Si falta una variable obligatoria o el tipo de dato es incorrecto (ej: un string en lugar de un entero), la aplicación aborta antes de arrancar, evitando comportamientos inesperados en producción.
* **🔒 Cifrado de Extremo a Extremo (AES-256):** Los archivos de esquema pueden cifrarse de forma simétrica (`schema.envql.enc`) permitiendo versionarlos de forma segura en Git. Solo se descifran con la llave maestra (`envql.key`) en tiempo de ejecución.
* **⚡ Generación Automática de Tipos (DX):** Genera interfaces nativas para TypeScript (`env.d.ts`) y Clases Tipadas para Python (`env_config.py`) para potenciar el autocompletado en tu IDE.
* **🌐 Agnóstico de Lenguaje:** Diseñado como un estándar universal para arquitecturas de microservicios políglotas.

---

## 📂 Estructura del Esquema (`schema.envql`)

Define tus variables, tipos y modificadores de seguridad en un archivo limpio y legible:

```envql
# Contrato de configuración de la aplicación
environment: String @default("development")
port: Int @default(3000)
database_url: String @secret
debug_mode: Boolean @default(false)
```

---

## 🚀 Guía de Inicio Rápido

### 1. Requisitos previos
Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

### 2. Inicializar el proyecto
```bash
python envql_cli.py init
```

### 3. Generar la llave maestra y cifrar
```bash
python envql_cli.py key:generate
python envql_cli.py encrypt --input schema.envql --output schema.envql.enc
```

### 4. Generar tipos para tu IDE (DX)
```bash
# Para proyectos TypeScript / Node.js (genera env.d.ts)
python envql_cli.py generate --target typescript

# Para proyectos Python (genera env_config.py con Dataclass tipada)
python envql_cli.py generate --target python
```

### 5. Validar y ejecutar la aplicación (Fail-Fast)
```bash
python envql_cli.py run python app.py
```

---

## 🗺️ Roadmap del Proyecto
- [x] Motor de parseo y validación de tipos básicos (Int, String, Boolean).
- [x] Capa de cifrado simétrico robusto (Fernet / AES-256).
- [x] Prototipo de CLI global (init, key:generate, encrypt, run).
- [x] Compiladores de tipos para TypeScript (`env.d.ts`) y Python (`env_config.py`).
- [ ] SDKs oficiales para Node.js, Python y Go.
- [ ] EnvQL Registry: Panel corporativo y sincronización en la nube (Versión Enterprise).

---

## 🤝 Contribuir
¡Las contribuciones son bienvenidas! Si quieres proponer mejoras, reportar bugs o crear SDKs para nuevos lenguajes, por favor abre un Issue o envía un Pull Request.

---

## 📄 Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
