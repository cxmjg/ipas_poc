#!/usr/bin/env python3
from nicegui import ui
from Assets import FuncionHora

nombreDeUsuario = 'Ramiro Sabetta'
rol = 'Estudiante'

with ui.header().classes(replace='row items-center') as header:
    ui.button(on_click=lambda: menuLateral.toggle(), icon='menu').props('flat color=white')

with ui.row().classes('w-full h-auto justify-center items-center fixed overflow-visible') as main:
    with ui.column().classes('items-center gap-3 h-auto'):
        ui.label('IPAS').classes('text-5xl font-bold text-blue-500')
        
        ui.label('Infraestructura Plataforma Ambiente Servicio').classes('text-lg text-gray-600 italic')
        
        ui.image('./Frontend/Images/Logo.png').classes('w-[250px] h-[250px]')
        
        ui.label('"Empieza A Programar Rápido, Desde Cualquier Lugar"').classes('text-base text-gray-700 italic')
        ui.label('Diseñado y desarrollado por Marcos García y Ramiro Sabetta').classes('text-sm text-gray-500')

with ui.left_drawer(value=False).classes('bg-blue-300 items-center justify-evenly z-40') as menuLateral:
    with ui.column() as contenedorBotones:
        ui.button('Mis Documentos').classes('w-[180px] h-auto text-center items-center')
        ui.button('Mis Contenedores').classes('w-[180px] h-auto text-center items-center')
        
    ui.separator().classes('my-4 border-t-2 border-gray-400')

    with ui.column().classes('items-center justify-center') as contenedorSeparador:
        with ui.column().classes('items-center') as contenedorUsuario:
            ui.icon('person', color='white').classes('text-[8em]')

        with ui.column().classes('items-center justify-center') as contenedorInfoUsuario:
            ui.label(nombreDeUsuario)
            ui.label(rol)

        with ui.column() as contenedorBoton:
            ui.button('Cerrar Sesión').classes('w-[180px] h-auto text-center items-center text-black')

with ui.footer().classes('w-full justify-end p-1') as footer:
    with ui.column().classes('gap-0 p-1') as contenedorFechaHora:
        labelHora = ui.label().classes('text-black')
        labelFecha = ui.label().classes('text-black')

def actualizarFechaHora():
    labelHora.text = FuncionHora.obtenerHora()
    labelFecha.text = FuncionHora.obtenerFecha()

ui.timer(1.0, actualizarFechaHora)



ui.run()