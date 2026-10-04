import os
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

def draw_header(c, width, height, current_slide, total_slides):
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(HexColor("#38BDF8"))
    c.drawString(60, height - 60, "EnvQL")
    
    c.setFont("Helvetica", 12)
    c.setFillColor(HexColor("#94A3B8"))
    c.drawString(120, height - 60, "|  Historias reales de produccion a las 2 AM")
    
    c.drawRightString(width - 60, height - 60, f"{current_slide} / {total_slides}")
    
    c.setStrokeColor(HexColor("#1E293B"))
    c.setLineWidth(1)
    c.line(60, height - 80, width - 60, height - 80)

def draw_footer(c, width, height):
    c.setStrokeColor(HexColor("#1E293B"))
    c.setLineWidth(1)
    c.line(60, 65, width - 60, 65)
    
    c.setFont("Helvetica", 11)
    c.setFillColor(HexColor("#64748B"))
    c.drawString(60, 44, "github.com/japuentem/envql   |   npm install envql")
    c.drawRightString(width - 60, 44, "Desliza para ver el desenlace ->")

def draw_card(c, x, y, w, h, bg_color="#1E293B", border_color="#334155", radius=12):
    c.setFillColor(HexColor(bg_color))
    c.setStrokeColor(HexColor(border_color))
    c.setLineWidth(1.5)
    c.roundRect(x, y, w, h, radius, fill=1, stroke=1)

def create_comic_carousel():
    pdf_path = r"D:\proyectos_personales\devops\envql\EnvQL_Comic_Carousel.pdf"
    img_panic = r"D:\proyectos_personales\devops\envql\assets_comic\dev_panic.png"
    
    size = 800
    c = canvas.Canvas(pdf_path, pagesize=(size, size))
    total_slides = 5

    # ====================================================
    # SLIDE 1: EL DRAMA NOCTURNO (COMIC ACT 1)
    # ====================================================
    c.setFillColor(HexColor("#0B0F17"))
    c.rect(0, 0, size, size, fill=1, stroke=0)
    draw_header(c, size, size, 1, total_slides)
    
    # Tag
    draw_card(c, 60, size - 160, 260, 38, bg_color="#311018", border_color="#EF4444", radius=8)
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(HexColor("#F87171"))
    c.drawString(75, size - 136, "BASADO EN HECHOS REALES")
    
    # Main Headline
    c.setFont("Helvetica-Bold", 34)
    c.setFillColor(HexColor("#F8FAFC"))
    c.drawString(60, size - 215, "2:14 AM en algun servidor...")
    
    # Comic Illustration
    if os.path.exists(img_panic):
        c.drawImage(img_panic, 130, 230, width=540, height=330, mask='auto')
        
    # Dialogue box below
    draw_card(c, 60, 95, size - 120, 115, bg_color="#0F172A", border_color="#334155", radius=12)
    c.setFont("Helvetica-Bold", 14); c.setFillColor(HexColor("#F59E0B"))
    c.drawString(85, 175, "Dev a las 5 PM:")
    c.setFont("Helvetica", 13); c.setFillColor(HexColor("#E2E8F0"))
    c.drawString(200, 175, "'El deploy paso verde en CI/CD, me voy a dormir tranquilo.'")
    
    c.setFont("Helvetica-Bold", 14); c.setFillColor(HexColor("#EF4444"))
    c.drawString(85, 140, "Slack a las 2 AM:")
    c.setFont("Helvetica", 13); c.setFillColor(HexColor("#FCA5A5"))
    c.drawString(215, 140, "@channel [CRITICAL] 500 Internal Server Error en checkout.")
    
    c.setFont("Helvetica-Oblique", 12); c.setFillColor(HexColor("#94A3B8"))
    c.drawString(85, 112, "El culpable: alguien tipeo DATABASE_URLL con doble L en el .env.")
    
    draw_footer(c, size, size)
    c.showPage()

    # ====================================================
    # SLIDE 2: EL DIALOGO DEL EQUIPO (COMIC ACT 2)
    # ====================================================
    c.setFillColor(HexColor("#0B0F17"))
    c.rect(0, 0, size, size, fill=1, stroke=0)
    draw_header(c, size, size, 2, total_slides)
    
    c.setFont("Helvetica-Bold", 32)
    c.setFillColor(HexColor("#F8FAFC"))
    c.drawString(60, size - 140, "Autopsia de un incidente clasico")
    c.setFont("Helvetica", 15)
    c.setFillColor(HexColor("#94A3B8"))
    c.drawString(60, size - 170, "40 minutos de panico para descubrir lo que nadie valido:")
    
    # Dialog Bubble 1: Tech Lead
    draw_card(c, 60, size - 310, size - 120, 115, bg_color="#0F172A", border_color="#38BDF8", radius=12)
    c.setFont("Helvetica-Bold", 16); c.setFillColor(HexColor("#38BDF8"))
    c.drawString(85, size - 230, "Tech Lead desesperado en videollamada:")
    c.setFont("Helvetica-Oblique", 14); c.setFillColor(HexColor("#F8FAFC"))
    c.drawString(85, size - 265, "— '¿Que rompieron ahora? ¿Se saturo el pool de la base de datos?")
    c.drawString(85, size - 290, "    ¿Se vencio el certificado SSL o cayo AWS?'")

    # Dialog Bubble 2: DevOps
    draw_card(c, 60, size - 445, size - 120, 115, bg_color="#0F172A", border_color="#F59E0B", radius=12)
    c.setFont("Helvetica-Bold", 16); c.setFillColor(HexColor("#FBBF24"))
    c.drawString(85, size - 365, "DevOps revisando los logs en vivo:")
    c.setFont("Helvetica-Oblique", 14); c.setFillColor(HexColor("#F8FAFC"))
    c.drawString(85, size - 400, "— 'No... la base de datos esta perfecta. Alguien subio un .env")
    c.drawString(85, size - 425, "    con DATABASE_URLL y el servidor arranco sin avisar a nadie.'")

    # Dialog Bubble 3: Servidor
    draw_card(c, 60, size - 580, size - 120, 115, bg_color="#18131E", border_color="#EF4444", radius=12)
    c.setFont("Helvetica-Bold", 16); c.setFillColor(HexColor("#F87171"))
    c.drawString(85, size - 500, "El Servidor Node.js / Python:")
    c.setFont("Helvetica-Oblique", 14); c.setFillColor(HexColor("#F8FAFC"))
    c.drawString(85, size - 535, "— 'A mi nadie me dijo que DATABASE_URL era obligatoria.")
    c.drawString(85, size - 560, "    Yo solo mori silenciosamente cuando el primer usuario entro.'")

    draw_footer(c, size, size)
    c.showPage()

    # ====================================================
    # SLIDE 3: POR QUE EL ARCHIVO .ENV ES UN MEME
    # ====================================================
    c.setFillColor(HexColor("#0B0F17"))
    c.rect(0, 0, size, size, fill=1, stroke=0)
    draw_header(c, size, size, 3, total_slides)
    
    c.setFont("Helvetica-Bold", 32)
    c.setFillColor(HexColor("#F8FAFC"))
    c.drawString(60, size - 140, "¿Por que .env sigue fallando en 2026?")
    c.setFont("Helvetica", 15)
    c.setFillColor(HexColor("#94A3B8"))
    c.drawString(60, size - 170, "Confiamos la configuracion mas critica a archivos ciegos:")
    
    # Issue 1
    draw_card(c, 60, size - 290, size - 120, 95, bg_color="#0F172A", border_color="#EF4444", radius=12)
    c.setFont("Helvetica-Bold", 16); c.setFillColor(HexColor("#F87171"))
    c.drawString(85, size - 225, "1. Cero Validacion Previa (No Fail-Fast)")
    c.setFont("Helvetica", 13); c.setFillColor(HexColor("#CBD5E1"))
    c.drawString(85, size - 252, "La app arranca contenta diciendo 'Listening on port 3000'...")
    c.drawString(85, size - 272, "y explota horas despues cuando alguien toca la ruta sin configurar.")

    # Issue 2
    draw_card(c, 60, size - 405, size - 120, 95, bg_color="#0F172A", border_color="#F59E0B", radius=12)
    c.setFont("Helvetica-Bold", 16); c.setFillColor(HexColor("#FBBF24"))
    c.drawString(85, size - 340, "2. La Trampa de los Booleanos")
    c.setFont("Helvetica", 13); c.setFillColor(HexColor("#CBD5E1"))
    c.drawString(85, size - 367, "En un .env pones DEBUG='false'...")
    c.drawString(85, size - 387, "¡y en JS 'false' se evalua como TRUE activando logs confidenciales!")

    # Issue 3
    draw_card(c, 60, size - 520, size - 120, 95, bg_color="#0F172A", border_color="#38BDF8", radius=12)
    c.setFont("Helvetica-Bold", 16); c.setFillColor(HexColor("#38BDF8"))
    c.drawString(85, size - 455, "3. Fugas de Secretos a Git")
    c.setFont("Helvetica", 13); c.setFillColor(HexColor("#CBD5E1"))
    c.drawString(85, size - 482, "Un simple 'git add .' accidental y tus credenciales de produccion")
    c.drawString(85, size - 502, "quedan indexadas para siempre en el historial de Git.")

    draw_footer(c, size, size)
    c.showPage()

    # ====================================================
    # SLIDE 4: ENTRA EL HEROE: ENVQL
    # ====================================================
    c.setFillColor(HexColor("#0B0F17"))
    c.rect(0, 0, size, size, fill=1, stroke=0)
    draw_header(c, size, size, 4, total_slides)
    
    c.setFont("Helvetica-Bold", 32)
    c.setFillColor(HexColor("#F8FAFC"))
    c.drawString(60, size - 140, "La Solucion: EnvQL al rescate")
    c.setFont("Helvetica", 15)
    c.setFillColor(HexColor("#94A3B8"))
    c.drawString(60, size - 170, "El contrato universal estricto que no deja pasar ni un error:")
    
    # Terminal block showing failure
    draw_card(c, 60, size - 390, size - 120, 195, bg_color="#030712", border_color="#334155", radius=12)
    c.setFillColor(HexColor("#EF4444")); c.circle(85, size - 220, 5, fill=1, stroke=0)
    c.setFillColor(HexColor("#F59E0B")); c.circle(100, size - 220, 5, fill=1, stroke=0)
    c.setFillColor(HexColor("#10B981")); c.circle(115, size - 220, 5, fill=1, stroke=0)
    c.setFont("Helvetica", 11); c.setFillColor(HexColor("#64748B")); c.drawString(140, size - 224, "terminal — npx envql run node app.js")

    c.setFont("Courier-Bold", 14)
    c.setFillColor(HexColor("#F8FAFC"))
    c.drawString(85, size - 260, "$ npx envql run node app.js")
    c.setFillColor(HexColor("#38BDF8"))
    c.drawString(85, size - 290, "[EnvQL Runtime] Validando entorno con esquema...")
    c.setFillColor(HexColor("#EF4444"))
    c.drawString(85, size - 320, "x Error: La variable obligatoria 'DATABASE_URL' no existe.")
    c.drawString(85, size - 350, "! Abortando ejecucion ANTES de iniciar.")

    # 2 Cards below
    draw_card(c, 60, 95, (size - 140)/2, 190, bg_color="#0F172A", border_color="#10B981", radius=12)
    c.setFont("Helvetica-Bold", 16); c.setFillColor(HexColor("#10B981"))
    c.drawString(85, 245, "[+] 0 ms Fail-Fast")
    c.setFont("Helvetica", 13); c.setFillColor(HexColor("#CBD5E1"))
    c.drawString(85, 210, "Si el contrato no se cumple,")
    c.drawString(85, 185, "la app NO arranca.")
    c.drawString(85, 160, "Imposible tener sorpresas")
    c.drawString(85, 135, "en produccion a las 2 AM.")

    draw_card(c, 60 + (size - 140)/2 + 20, 95, (size - 140)/2, 190, bg_color="#0F172A", border_color="#38BDF8", radius=12)
    c.setFont("Helvetica-Bold", 16); c.setFillColor(HexColor("#38BDF8"))
    c.drawString(430, 245, "✓ Cifrado AES-256")
    c.setFont("Helvetica", 13); c.setFillColor(HexColor("#CBD5E1"))
    c.drawString(430, 210, "Esquemas cifrados seguros")
    c.drawString(430, 185, "para commitear en Git.")
    c.drawString(430, 160, "Descifrado transparente")
    c.drawString(430, 135, "solo en memoria.")

    draw_footer(c, size, size)
    c.showPage()

    # ====================================================
    # SLIDE 5: CTA CON ESTILO COMIC TECH
    # ====================================================
    c.setFillColor(HexColor("#0B0F17"))
    c.rect(0, 0, size, size, fill=1, stroke=0)
    draw_header(c, size, size, 5, total_slides)
    
    draw_card(c, 60, 180, size - 120, 500, bg_color="#0F172A", border_color="#6366F1", radius=16)
    
    c.setFont("Helvetica-Bold", 34)
    c.setFillColor(HexColor("#F8FAFC"))
    c.drawCentredString(size/2, 620, "Dile adios a las caidas por .env")
    
    c.setFont("Helvetica", 16)
    c.setFillColor(HexColor("#94A3B8"))
    c.drawCentredString(size/2, 575, "EnvQL ya esta disponible en NPM (v0.1.0) y GitHub.")
    c.drawCentredString(size/2, 545, "100% Open Source bajo Licencia MIT.")

    # Terminal NPM Install
    draw_card(c, 100, 360, size - 200, 140, bg_color="#030712", border_color="#334155", radius=10)
    c.setFont("Helvetica-Bold", 15); c.setFillColor(HexColor("#FBBF24"))
    c.drawString(130, 465, "Pruébalo en tu proyecto en 30 segundos:")
    c.setFont("Courier-Bold", 16); c.setFillColor(HexColor("#38BDF8"))
    c.drawString(130, 425, "npm install envql")
    c.drawString(130, 390, "npx envql init")

    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(HexColor("#F8FAFC"))
    c.drawCentredString(size/2, 305, "¿Te ha pasado algo parecido?")
    
    c.setFont("Helvetica", 15)
    c.setFillColor(HexColor("#CBD5E1"))
    c.drawCentredString(size/2, 265, "Cuentame tu peor anecdota con un .env en los comentarios")
    
    c.setFont("Helvetica-Bold", 17)
    c.setFillColor(HexColor("#818CF8"))
    c.drawCentredString(size/2, 215, "github.com/japuentem/envql   |   npmjs.com/package/envql")

    draw_footer(c, size, size)
    c.showPage()
    
    c.save()
    print(f"Comic Carousel generated successfully at: {pdf_path}")

if __name__ == "__main__":
    create_comic_carousel()
