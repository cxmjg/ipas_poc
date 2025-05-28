import docker

client = docker.DockerClient(base_url='tcp://127.0.0.1:2375')

def descargarImagen(repositorio, tag='latest'):
    imagenes = client.images.list()
    if repositorio not in imagenes:
        imagen = client.images.pull(repositorio, tag)
    return imagen

def listarContenedores():
    for contenedor in client.containers.list(all=True):
        print(contenedor.name)

def eliminarContenedores():
    for contenedor in client.containers.list(all=True):
        contenedor.remove()

def crearContenedor(imagen, nombre, comandos=[]):
    client.containers.create(image=imagen, command=comandos, name=nombre)

def ejecutarContenedor(nombre):
    client.containers.run(nombre)


crearContenedor(descargarImagen('lscr.io/linuxserver/vscodium'), 'vscodium')
listarContenedores()