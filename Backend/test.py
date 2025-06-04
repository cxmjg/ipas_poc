from DockerDriver import DockerDriver

docker = DockerDriver()

contenedor = {
    'imagen':'lscr.io/linuxserver/webtop',
    'nombre': 'webtop',
    'puertos': {
        '3000/tcp': 3000,
        '3001/tcp': 3001
    }
}


if docker.existeContenedor(contenedor['nombre']):
    docker.eliminarContenedor(contenedor['nombre'])

docker.crearContenedor(docker.descargarImagen(contenedor['imagen']), contenedor['nombre'], puertos=contenedor['puertos'])

print(docker.detenerContenedor(contenedor['nombre']))

print(docker.ejecutarContenedor(contenedor['nombre']))

print(docker.reiniciarContenedor(contenedor['nombre']))

print(docker.getSalud(contenedor['nombre']))

print('El contenedor puede ser accedido utilizando la siguiente url: http://localhost:3000')