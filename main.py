from nicegui import ui

encendido = False

def cambiar_estado():
    global encendido

    encendido = not encendido

    if encendido:
        estado.text = "Estado actual: ON"
        estado.style('color: green; font-size: 24px')
    else:
        estado.text = "Estado actual: OFF"
        estado.style('color: red; font-size: 24px')


with ui.column().classes('w-full h-screen items-center justify-center'):
    
    


    with ui.card().style('width:300px; background-color:blue;').classes('items-center'):

        ui.label('Mi Primera App').style(
            'font-size: 24px; font-weight: bold'
        )
        
        ui.image(
        'nice.png'
    ).style('width:250px')

        estado = ui.label(
            "Estado actual: Apagado"
        ).style(
            'color: red; font-size: 24px'
        )

        ui.button(
            'Cambiar Estado',
            icon='lightbulb',
            color='black',
            on_click=cambiar_estado
        ).style('color: white')

ui.run()