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
    'Mis Documentos':None,
    'Mis Contenedores': None
}

columns = [
    {'name': 'nombre', 'label': 'Nombre', 'field': 'nombre', 'required': True, 'align': 'left'},
    {'name': 'imagen', 'label': 'Imagen', 'field': 'imagen', 'sortable': True},
    {'name': 'estado', 'label': 'Estado', 'field': 'estado', 'sortable': True, 'align': 'center'},
    {'name': 'puertos', 'label': 'Puertos', 'field': 'puertos', 'sortable': True, 'align': 'center'},
    {'name': 'link', 'label': 'Link', 'field': 'link', 'sortable': True, 'align': 'center'},
]
rows = [
    {'nombre': 'Escritorio XFCE', 'imagen': 'webtop', 'estado':'Activo', 'puertos': 3000, 'link':'http://localhost:3000'},
    {'nombre': 'Base MySQL', 'imagen': 'mysql', 'estado':'Detenido', 'puertos': '', 'link':''},
    {'nombre': 'Servidor WEB', 'imagen': 'apache', 'estado':'Detenido', 'puertos': '', 'link':''},
]

menuLateral = MenuLateral(opcionesMenu, usuario)
header = Header(menuLateral.getMenuLateral(), None)
header.getHeader()

with html.section().classes('w-full justify-evenly') as main:
    
    with ui.row().classes('items-center justify-center p-0 m-0 gap-0 flex-col sm:flex-row ') as home:
        ui.label('Empieza a Programar Rápido, Desde Cualquier Lugar').classes('text-center sm:text-left text-3xl lg:text-7xl md:text-5xl w-[50%] font-extrabold font-sans')
        
        ui.image('./Frontend/Images/Logo.png').classes('w-[35%] p-0 m-0')
    
    with ui.column().classes('w-50 justify-evenly items-center') as misContenedores:
        contenedores = ui.table(columns=columns, rows=rows, row_key='nombre').classes('text-black text-center')
        contenedores.add_slot('body-cell-estado', '''
            <q-td :props="props">
                <q-badge :color="props.value == 'Detenido' ? 'red' : 'green'">
                    {{ props.value }}
                </q-badge>
            </q-td>
        ''')
        contenedores.add_slot('body-cell-link', '''
            <q-td :props="props">
                <a :href="props.value" target="_blank" v-if="props.value">ABRIR</a>
            </q-td>
        ''')
    

misContenedores.set_visibility(visible=False)
footer = Footer()
footer.getFooter()
ui.timer(1.0, footer.actualizarFechaHora)

def goToHome():
    home.set_visibility(visible=True)
    misContenedores.set_visibility(visible=False)
    menuLateral.getMenuLateral().hide()

def mostrarContenedores():
    home.set_visibility(visible=False)
    misContenedores.set_visibility(visible=True)

menuLateral.setOpciones({'nombre': 'Mis Contenedores', 'accion': mostrarContenedores})

header.setGoToHome(goToHome)

ui.run()