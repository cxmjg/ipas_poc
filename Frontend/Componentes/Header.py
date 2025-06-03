from nicegui import ui, html

class Header:
    def __init__(self, menuLateral_):
        with ui.header().classes('items-center p-0') as self.header:
            ui.button(on_click=menuLateral_.toggle, icon='menu').props('flat color=white')
            with ui.row().classes('items-center'):
                html.h1('IPAS').classes('text-5xl font-extrabold font-sans')
                ui.html('<h2>Infraestructura Plataforma Ambiente Servicio</h2>').classes('text-lg text-gray-600 italic')

    def getHeader(self):
        return self.header