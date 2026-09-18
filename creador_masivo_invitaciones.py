import generador_invitaciones

with open('datos_invitaciones.txt', mode='rt', encoding='utf-8') as fichero:
    for datos_invitacion in fichero:
        datos_invitacion = datos_invitacion.strip() # Eliminar el salto línea final
        nombre_fichero, evento, imagen, fecha, direccion = datos_invitacion.split('#')
        generador_invitaciones.generar_invitacion(nombre_fichero.lower().replace(' ','_')+'.pdf',
                                                  evento, imagen, fecha, direccion)