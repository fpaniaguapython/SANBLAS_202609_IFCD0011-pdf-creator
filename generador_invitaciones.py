from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm, inch

def generar_invitacion(nombre_fichero : str, 
                       tipo_evento : str,
                       nombre_imagen : str,
                       fecha : str,
                       direccion : str):
    
    # Tamaño
    canvas = Canvas(nombre_fichero, pagesize=(20 * cm, 12 * cm))

    canvas.drawImage(
    "frame.png",
    x=-20,
    y=-10,
    width=608,
    height=370,
    preserveAspectRatio=False,
    mask="auto")

    canvas.drawImage(
        nombre_imagen,
        x=170, y=20,
        width=200, height=200,
        preserveAspectRatio=True,
        mask="auto")

    canvas.setFont("Times-Roman", 24)
    canvas.drawString(70, 250, 'ESTÁS INVITADO A UNA FIESTA DE..')
    canvas.setFont("Times-Roman", 48)
    canvas.drawString(140, 200, tipo_evento.upper())

    canvas.setFont("Times-Roman", 20)
    canvas.drawString(50, 60, fecha)
    canvas.drawString(50, 40, direccion)
    canvas.save()