#!/usr/bin/env python3
from nicegui import ui, html
from Componentes.Footer import Footer
from Componentes.Header import Header
from Componentes.MenuLateral import MenuLateral


def mostrarAlerta(texto= 'Clik!'):
    ui.notification(texto)

usuario = {
    'nombre': 'Ramiro Sabetta',
    'rol': 'Estudiante'
}

opcionesMenu = {
    'Mis Documentos':mostrarAlerta,
    'Mis Contenedores': mostrarAlerta
}

menuLateral = MenuLateral(opcionesMenu, usuario).getMenuLateral()
header = Header(menuLateral)
header.getHeader()

with ui.row().classes('items-center justify-center p-0 m-0 gap-0 flex-col sm:flex-row ') as main:
    ui.label('Empieza a Programar Rápido, Desde Cualquier Lugar').classes('text-center sm:text-left text-3xl lg:text-7xl md:text-5xl w-[50%] font-extrabold font-sans')
    ui.image('./Frontend/Images/Logo.png').classes('w-[35%] p-0 m-0')


footer = Footer()
footer.getFooter()
ui.timer(1.0, footer.actualizarFechaHora)


ui.run()