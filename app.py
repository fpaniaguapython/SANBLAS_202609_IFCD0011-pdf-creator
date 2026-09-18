import generador_invitaciones

print('Comenzando la ejecución del programa...')

tipo_evento = input('Tipo de evento:')
nombre_imagen = input('Nombre imagen:')
fecha = input('Fecha:')
direccion = input('Dirección:')

generador_invitaciones.generar_invitacion(
    tipo_evento.lower().replace(' ','_')+'.pdf',
    tipo_evento, nombre_imagen, fecha, direccion)

# generador_invitaciones.generar_invitacion(
#     'despedida.pdf',
#     'Despedida', None, '17-10-2026', 'Pub La Movida. C/ Desengaño, 15')




