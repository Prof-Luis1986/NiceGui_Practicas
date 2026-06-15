from nicegui import ui

encendido = False

estado = ui.label('Apagado')

def cambiar_estado():
    global encendido

    encendido = not encendido

    if encendido:
        estado.text = 'Encendido'
        boton.props('color=green')
    else:
        estado.text = 'Apagado'
        boton.props('color=red')

boton = ui.button(
    'Cambiar estado',
    on_click=cambiar_estado,
    color='red'
)

ui.run()