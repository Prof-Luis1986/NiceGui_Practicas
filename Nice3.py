from nicegui import ui

encendido = False
estado = ui.label('Estado actual: Apagado')

def cambiar_estado():
    global encendido

    encendido = not encendido

    if encendido:
        estado.text = 'Estado actual: Encendido'
        estado.style('color: green; font-size: 24px')
    else:
        estado.text = 'Estado actual: Apagado'
        estado.style('color: red; font-size: 24px')

ui.button('Cambiar estado', on_click=cambiar_estado)

ui.run()