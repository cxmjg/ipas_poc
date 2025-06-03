from DockerDriver import DockerDriver

docker = DockerDriver()

webtopEnv = {}

webtopPorts = {
    '3000/tcp': 3000,
    '3001/tcp': 3001
}

if docker.existeContenedor('webtop'):
    docker.eliminarContenedor('webtop')

docker.crearContenedor(docker.descargarImagen('lscr.io/linuxserver/webtop'), 'webtop', puertos=webtopPorts)

print(docker.detenerContenedor('webtop'))

print(docker.ejecutarContenedor('webtop'))

print(docker.reiniciarContenedor('webtop'))

print(docker.getSalud('webtop'))

print('El contenedor puede ser accedido utilizando la siguiente url: http://localhost:3000')