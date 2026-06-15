from nicegui import ui

# Creamos un label inicial
estado = ui.label('Estado actual: Apagado')

# Creamos una función que cambiará el texto del label
def cambiar_estado():
    estado.text = 'Estado actual: Encendido'

# Creamos un botón que ejecuta la función
ui.button('Cambiar estado', on_click=cambiar_estado)

# Ejecutamos la aplicación
ui.run()