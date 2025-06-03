from nicegui import ui

class MenuLateral:
    def __init__(self, opciones, usuario):
        with ui.left_drawer(value=False).classes('bg-blue-300 items-center justify-evenly z-40').props('overlay') as self.menuLateral:
            
            with ui.column() as contenedorBotones:
                for opcion in opciones.keys():
                    ui.button(opcion, on_click= lambda: opciones[opcion]()).classes('w-[180px] h-auto text-center items-center')

            ui.separator()

            with ui.column().classes('items-center') as contenedorUsuario:
                ui.icon('person', color='white').classes('text-[8em]')

            with ui.column().classes('items-center justify-center') as contenedorInfoUsuario:
                ui.label(usuario['nombre'])
                ui.label(usuario['rol'])

            with ui.column() as contenedorBoton:
                ui.button('Cerrar Sesión').classes('w-[180px] h-auto text-center items-center text-black')

    def getMenuLateral(self):
        return self.menuLateral