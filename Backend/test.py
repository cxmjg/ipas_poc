from DockerDriver import DockerDriver

docker = DockerDriver()

contenedor = {
    'imagen':'lscr.io/linuxserver/webtop',
    'nombre': 'webtop',
    'puertos': {
        '3000/tcp': 3000,
        '3001/tcp': 3001
    },
    'ambiente':{
        'LC_ALL': 'es_ES.UTF-8',
        'TITLE' : 'Ambiente XFCE',
        'CUSTOM_USER': 'ramirosabetta',
        'PASSWORD': '1234'
    },
    'volumenes': {
        '/home/mgarcia/Ambiente/': {
            'bind': '/config',
            'mode': 'rw',
        },
    },
    'comandos': 'mkdir /home/ejemplo'
}

def getLinks(contenedor):
    puertos = list(contenedor['puertos'].values())
    ip = docker.getIp(contenedor['nombre'])
    links = ''
    for puerto in puertos:
        links += f'http://{ip}:{puerto} '    
    return links

if docker.existeContenedor(contenedor['nombre']):
    docker.eliminarContenedor(contenedor['nombre'])

docker.crearContenedor(docker.descargarImagen(contenedor['imagen']), contenedor['nombre'], puertos=contenedor['puertos'], env=contenedor['ambiente'], vol=contenedor['volumenes'], comandos=contenedor['comandos'])

print(docker.detenerContenedor(contenedor['nombre']))

print(docker.ejecutarContenedor(contenedor['nombre']))

print(docker.reiniciarContenedor(contenedor['nombre']))

print(docker.getSalud(contenedor['nombre']))

print(f'El contenedor puede ser accedido utilizando las siguientes urls: {getLinks(contenedor)}')