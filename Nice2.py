from nicegui import ui

encendido = False
estado = ui.label('Estado actual: Apagado')

def cambiar_estado():
    global encendido

    encendido = not encendido

    if encendido:
        estado.text = 'Estado actual: Encendido'
    else:
        estado.text = 'Estado actual: Apagado'

ui.button('Cambiar estado', on_click=cambiar_estado)

ui.run()