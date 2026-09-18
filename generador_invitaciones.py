from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm

def generar_invitacion(nombre_fichero : str, 
                       tipo_evento : str,
                       nombre_imagen : str,
                       fecha : str,
                       direccion : str):
    """
    Genera una invitación para una fiesta y la guarda como archivo PDF.

    La invitación incluye un marco decorativo, una imagen asociada al evento,
    el tipo de evento, la fecha y la dirección.

    Args:
        nombre_fichero (str): Nombre y ruta del archivo PDF que se generará.
        tipo_evento (str): Tipo de evento o fiesta que aparecerá en la invitación.
        nombre_imagen (str): Nombre o ruta de la imagen que se incluirá.
        fecha (str): Fecha del evento que se mostrará en la invitación.
        direccion (str): Dirección donde tendrá lugar el evento.

    Returns:
        None: La función genera y guarda el archivo PDF, pero no devuelve ningún valor.

    Raises:
        FileNotFoundError: Si no se encuentra la imagen especificada.
        OSError: Si ocurre un error al crear o guardar el archivo PDF.
    """
    
    # Tamaño
    canvas = Canvas(nombre_fichero, pagesize=(20 * cm, 12 * cm))

    canvas.drawImage(
        "frame.png",
        x=-20, y=-10,
        width=608, height=370,
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