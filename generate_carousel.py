import os
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

def draw_header(c, width, height, current_slide, total_slides):
    # Top bar badge
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(HexColor("#38BDF8")) # Sky blue
    c.drawString(60, height - 60, "EnvQL")
    
    c.setFont("Helvetica", 12)
    c.setFillColor(HexColor("#94A3B8"))
    c.drawString(120, height - 60, "|  The Universal Configuration Standard")
    
    # Slide count
    c.drawRightString(width - 60, height - 60, f"{current_slide} / {total_slides}")
    
    # Separator line
    c.setStrokeColor(HexColor("#1E293B"))
    c.setLineWidth(1)
    c.line(60, height - 80, width - 60, height - 80)

def draw_footer(c, width, height):
    c.setStrokeColor(HexColor("#1E293B"))
    c.setLineWidth(1)
    c.line(60, 70, width - 60, 70)
    
    c.setFont("Helvetica", 11)
    c.setFillColor(HexColor("#64748B"))
    c.drawString(60, 48, "github.com/japuentem/envql")
    c.drawRightString(width - 60, 48, "Desliza para ver mas ->")

def draw_card(c, x, y, w, h, bg_color="#1E293B", border_color="#334155", radius=12):
    c.setFillColor(HexColor(bg_color))
    c.setStrokeColor(HexColor(border_color))
    c.setLineWidth(1.5)
    c.roundRect(x, y, w, h, radius, fill=1, stroke=1)

def create_carousel():
    pdf_path = r"D:\proyectos_personales\devops\envql\EnvQL_LinkedIn_Carousel.pdf"
    
    size = 800
    c = canvas.Canvas(pdf_path, pagesize=(size, size))
    total_slides = 5
    
    # ====================================================
    # SLIDE 1: PORTADA IMPACTANTE
    # ====================================================
    c.setFillColor(HexColor("#0B0F17"))
    c.rect(0, 0, size, size, fill=1, stroke=0)
    
    draw_header(c, size, size, 1, total_slides)
    
    # Badge (adjusted width to 280)
    draw_card(c, 60, size - 170, 280, 42, bg_color="#1E1B4B", border_color="#6366F1", radius=8)
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(HexColor("#A5B4FC"))
    c.drawString(75, size - 144, "DEVOPS & SOFTWARE ARCHITECTURE")
    
    # Title
    c.setFont("Helvetica-Bold", 38)
    c.setFillColor(HexColor("#F8FAFC"))
    c.drawString(60, size - 240, "¿Por que un simple archivo")
    c.setFillColor(HexColor("#EF4444"))
    c.drawString(60, size - 290, ".env")
    c.setFillColor(HexColor("#F8FAFC"))
    c.drawString(170, size - 290, "sigue tirando produccion?")
    
    # Subtitle
    c.setFont("Helvetica", 18)
    c.setFillColor(HexColor("#94A3B8"))
    c.drawString(60, size - 350, "Descubre como erradicar los typos fatales, fugas de secretos")
    c.drawString(60, size - 378, "y la falta de tipado estricto en el software moderno.")
    
    # Big Feature Card
    draw_card(c, 60, 140, size - 120, 180, bg_color="#0F172A", border_color="#38BDF8", radius=16)
    c.setFont("Helvetica-Bold", 26)
    c.setFillColor(HexColor("#38BDF8"))
    c.drawString(90, 265, "Presentando: EnvQL")
    
    c.setFont("Helvetica", 16)
    c.setFillColor(HexColor("#CBD5E1"))
    c.drawString(90, 225, "El contrato universal declarativo y cifrado (AES-256) que une")
    c.drawString(90, 195, "la seguridad y la validacion estricta antes del arranque.")
    
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(HexColor("#22C55E"))
    c.drawString(90, 160, "[+] Fail-Fast    [+] Cifrado AES-256    [+] Tipos TS y Python    [+] Open Source")
    
    draw_footer(c, size, size)
    c.showPage()
    
    # ====================================================
    # SLIDE 2: EL PROBLEMA HISTORICO
    # ====================================================
    c.setFillColor(HexColor("#0B0F17"))
    c.rect(0, 0, size, size, fill=1, stroke=0)
    draw_header(c, size, size, 2, total_slides)
    
    c.setFont("Helvetica-Bold", 32)
    c.setFillColor(HexColor("#F8FAFC"))
    c.drawString(60, size - 140, "La configuracion actual es fragil")
    c.setFont("Helvetica", 16)
    c.setFillColor(HexColor("#94A3B8"))
    c.drawString(60, size - 170, "Durante 25 anos hemos manejado variables criticas a ciegas:")
    
    # Pain point 1
    draw_card(c, 60, size - 310, size - 120, 110, bg_color="#18131E", border_color="#EF4444", radius=12)
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(HexColor("#F87171"))
    c.drawString(90, size - 240, "1. Caidas por Typo Silencioso")
    c.setFont("Helvetica", 14)
    c.setFillColor(HexColor("#CBD5E1"))
    c.drawString(90, size - 270, "Un simple 'DATABASE_URLL' pasa desapercibido hasta que un cliente")
    c.drawString(90, size - 290, "toca esa ruta y tumba el servicio en plena madrugada.")
    
    # Pain point 2
    draw_card(c, 60, size - 440, size - 120, 110, bg_color="#18131E", border_color="#F59E0B", radius=12)
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(HexColor("#FBBF24"))
    c.drawString(90, size - 370, "2. Sin Validacion de Tipos (Type Safety)")
    c.setFont("Helvetica", 14)
    c.setFillColor(HexColor("#CBD5E1"))
    c.drawString(90, size - 400, "Un PORT que llega como string '3000' o DEBUG='false' evaluado como")
    c.drawString(90, size - 420, "booleano verdadero causa comportamientos erraticos y bugs graves.")
    
    # Pain point 3
    draw_card(c, 60, size - 570, size - 120, 110, bg_color="#18131E", border_color="#EF4444", radius=12)
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(HexColor("#F87171"))
    c.drawString(90, size - 500, "3. Fuga Accidental de Secretos")
    c.setFont("Helvetica", 14)
    c.setFillColor(HexColor("#CBD5E1"))
    c.drawString(90, size - 530, "Archivos .env subidos a repositorios publicos por descuidos en el .gitignore,")
    c.drawString(90, size - 550, "comprometiendo llaves de APIs, tokens y credenciales de bases de datos.")
    
    draw_footer(c, size, size)
    c.showPage()
    
    # ====================================================
    # SLIDE 3: LA SOLUCION - ENVQL
    # ====================================================
    c.setFillColor(HexColor("#0B0F17"))
    c.rect(0, 0, size, size, fill=1, stroke=0)
    draw_header(c, size, size, 3, total_slides)
    
    c.setFont("Helvetica-Bold", 32)
    c.setFillColor(HexColor("#F8FAFC"))
    c.drawString(60, size - 140, "La Solucion: Un Contrato Estricto")
    c.setFont("Helvetica", 16)
    c.setFillColor(HexColor("#94A3B8"))
    c.drawString(60, size - 170, "Asi como GraphQL unifico las APIs, EnvQL unifica el entorno.")
    
    # Code box mockup
    draw_card(c, 60, size - 410, size - 120, 210, bg_color="#030712", border_color="#1E293B", radius=12)
    
    c.setFillColor(HexColor("#EF4444")); c.circle(85, size - 225, 5, fill=1, stroke=0)
    c.setFillColor(HexColor("#F59E0B")); c.circle(100, size - 225, 5, fill=1, stroke=0)
    c.setFillColor(HexColor("#10B981")); c.circle(115, size - 225, 5, fill=1, stroke=0)
    c.setFont("Helvetica", 11); c.setFillColor(HexColor("#64748B")); c.drawString(140, size - 229, "schema.envql")
    
    c.setFont("Courier-Bold", 15)
    c.setFillColor(HexColor("#38BDF8"))
    c.drawString(85, size - 265, "environment: String @default(\"development\")")
    c.drawString(85, size - 295, "port:        Int    @default(3000)")
    c.drawString(85, size - 325, "database_url: String @secret")
    c.drawString(85, size - 355, "debug_mode:  Boolean @default(false)")
    
    # Highlights below code
    draw_card(c, 60, 110, (size - 140)/2, 180, bg_color="#0F172A", border_color="#38BDF8", radius=12)
    c.setFont("Helvetica-Bold", 16); c.setFillColor(HexColor("#38BDF8"))
    c.drawString(80, 255, "Tipado Estricto")
    c.setFont("Helvetica", 13); c.setFillColor(HexColor("#CBD5E1"))
    c.drawString(80, 220, "• String, Int, Boolean.")
    c.drawString(80, 190, "• Modificador @default.")
    c.drawString(80, 160, "• Falla antes de arrancar.")
    c.drawString(80, 130, "• Cero sorpresas en prod.")
    
    draw_card(c, 60 + (size - 140)/2 + 20, 110, (size - 140)/2, 180, bg_color="#0F172A", border_color="#10B981", radius=12)
    c.setFont("Helvetica-Bold", 16); c.setFillColor(HexColor("#10B981"))
    c.drawString(430, 255, "Cifrado Simetrico")
    c.setFont("Helvetica", 13); c.setFillColor(HexColor("#CBD5E1"))
    c.drawString(430, 220, "• Cifrado AES-256 (Fernet).")
    c.drawString(430, 190, "• Seguro para guardar en Git.")
    c.drawString(430, 160, "• Descifra solo en memoria.")
    c.drawString(430, 130, "• Protegido por llave maestra.")
    
    draw_footer(c, size, size)
    c.showPage()
    
    # ====================================================
    # SLIDE 4: CARACTERISTICAS & DX
    # ====================================================
    c.setFillColor(HexColor("#0B0F17"))
    c.rect(0, 0, size, size, fill=1, stroke=0)
    draw_header(c, size, size, 4, total_slides)
    
    c.setFont("Helvetica-Bold", 32)
    c.setFillColor(HexColor("#F8FAFC"))
    c.drawString(60, size - 140, "Developer Experience (DX) Total")
    c.setFont("Helvetica", 16)
    c.setFillColor(HexColor("#94A3B8"))
    c.drawString(60, size - 170, "Un ecosistema de herramientas disenado para el dia a dia:")
    
    # Feature 1
    draw_card(c, 60, size - 290, size - 120, 95, bg_color="#0F172A", border_color="#38BDF8", radius=12)
    c.setFont("Helvetica-Bold", 17); c.setFillColor(HexColor("#38BDF8"))
    c.drawString(85, size - 225, "1. CLI Potente e Intuitivo")
    c.setFont("Helvetica", 13); c.setFillColor(HexColor("#CBD5E1"))
    c.drawString(85, size - 250, "Comandos agiles: 'envql init', 'envql key:generate' y 'envql encrypt'")
    c.drawString(85, size - 270, "para integrar facilmente en tus scripts de CI/CD.")
    
    # Feature 2
    draw_card(c, 60, size - 405, size - 120, 95, bg_color="#0F172A", border_color="#A855F7", radius=12)
    c.setFont("Helvetica-Bold", 17); c.setFillColor(HexColor("#C084FC"))
    c.drawString(85, size - 340, "2. Generacion de Tipos para IDEs")
    c.setFont("Helvetica", 13); c.setFillColor(HexColor("#CBD5E1"))
    c.drawString(85, size - 365, "Crea definiciones automaticas para autocompletado nativo:")
    c.drawString(85, size - 385, "TypeScript (env.d.ts) y Python (Dataclasses inmutables).")
    
    # Feature 3
    draw_card(c, 60, size - 520, size - 120, 95, bg_color="#0F172A", border_color="#10B981", radius=12)
    c.setFont("Helvetica-Bold", 17); c.setFillColor(HexColor("#34D399"))
    c.drawString(85, size - 455, "3. Ejecutor Seguro: envql run")
    c.setFont("Helvetica", 13); c.setFillColor(HexColor("#CBD5E1"))
    c.drawString(85, size - 480, "Valida el entorno criptograficamente en memoria y solo si el")
    c.drawString(85, size - 500, "contrato se cumple al 100%, ejecuta tu aplicacion.")
    
    draw_footer(c, size, size)
    c.showPage()
    
    # ====================================================
    # SLIDE 5: LLAMADO A LA ACCION (CTA)
    # ====================================================
    c.setFillColor(HexColor("#0B0F17"))
    c.rect(0, 0, size, size, fill=1, stroke=0)
    draw_header(c, size, size, 5, total_slides)
    
    draw_card(c, 60, 200, size - 120, 470, bg_color="#0F172A", border_color="#6366F1", radius=16)
    
    c.setFont("Helvetica-Bold", 34)
    c.setFillColor(HexColor("#F8FAFC"))
    c.drawCentredString(size/2, 600, "¡Unete a la revolucion Open Source!")
    
    c.setFont("Helvetica", 16)
    c.setFillColor(HexColor("#94A3B8"))
    c.drawCentredString(size/2, 555, "EnvQL es de codigo abierto bajo Licencia MIT.")
    c.drawCentredString(size/2, 530, "Construyamos juntos el proximo estandar de la industria.")
    
    # Steps
    draw_card(c, 100, 340, size - 200, 150, bg_color="#030712", border_color="#334155", radius=10)
    c.setFont("Helvetica-Bold", 16); c.setFillColor(HexColor("#FBBF24"))
    c.drawString(130, 450, "Como empezar hoy:")
    c.setFont("Courier", 14); c.setFillColor(HexColor("#38BDF8"))
    c.drawString(130, 415, "git clone https://github.com/japuentem/envql.git")
    c.drawString(130, 385, "pip install -r requirements.txt")
    c.drawString(130, 355, "python envql_secure.py")
    
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(HexColor("#F8FAFC"))
    c.drawCentredString(size/2, 280, "¿Te gusto el proyecto? Apoyanos con una estrella en GitHub")
    
    c.setFont("Helvetica-Bold", 17)
    c.setFillColor(HexColor("#818CF8"))
    c.drawCentredString(size/2, 235, "github.com/japuentem/envql")
    
    c.setFont("Helvetica", 13)
    c.setFillColor(HexColor("#64748B"))
    c.drawCentredString(size/2, 100, "Deja tu opinion en los comentarios: ¿Como validas tus variables hoy?")
    
    draw_footer(c, size, size)
    c.showPage()
    c.save()
    print(f"Carrusel generado exitosamente en: {pdf_path}")

if __name__ == "__main__":
    create_carousel()
