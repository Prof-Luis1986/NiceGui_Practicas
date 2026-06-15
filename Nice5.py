from nicegui import ui

encendido = False

def cambiar_estado():
    global encendido

    encendido = not encendido

    if encendido:
        estado.text = "Estado actual: ON"
        estado.style('color: green; font-size: 24px')
        boton.set_text('Apagar')
        boton.props('color=green')
    else:
        estado.text = "Estado actual: OFF"
        estado.style('color: red; font-size: 24px')
        boton.set_text('Encender')
        boton.props('color=red')


with ui.column().classes('w-full h-screen items-center justify-center'):

    with ui.card().style(
        'width:300px; background-color:blue; color:white;'
    ).classes('items-center'):

        ui.label('Mi Primera App').style(
            'font-size: 24px; font-weight: bold'
        )

        estado = ui.label(
            "Estado actual: OFF"
        ).style(
            'color: red; font-size: 24px'
        )

        boton = ui.button(
            'Encender',
            icon='lightbulb',
            color='red',
            on_click=cambiar_estado
        ).style('color: white')

ui.run()