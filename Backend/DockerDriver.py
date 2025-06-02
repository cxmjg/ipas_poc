import docker

class DockerDriver:
    def __init__(self, base_url='tcp://127.0.0.1:2375'):
        self.client = docker.DockerClient(base_url=base_url)

    def descargar_imagen(self, repositorio, tag='latest'):
        print('Buscando imagen...')
        imagenes = self.client.images.list(name=repositorio)
        if len(imagenes) == 0:
            print('Imagen no existe, iniciando proceso de descarga...')
            imagen = self.client.images.pull(repositorio, tag)
        else:
            print('Imagen existe')
            imagen = self.client.images.get(repositorio)
        print('Finalizado')
        return imagen

    def listar_contenedores(self):
       return self.client.containers.list(all=True)

    def eliminar_contenedores(self):
        for contenedor in self.client.containers.list(all=True):
            contenedor.remove()

    def crear_contenedor(self, imagen, nombre, comandos=None, env=None, puertos=None):
        if comandos is None:
            comandos = []
        if env is None:
            env = {}
        if puertos is None:
            puertos = {}
        return self.client.containers.create(image=imagen, command=comandos, name=nombre, ports=puertos, environment=env)

    def ejecutar_contenedor(self, nombre):
        contenedor = self.client.containers.get(nombre)
        contenedor.start()
        return contenedor.status

    def detener_contenedor(self, nombre):
        contenedor = self.client.containers.get(nombre)
        contenedor.stop()
        return contenedor.status
    

webtopEnv = {

}

webtopPorts = {
    '3000/tcp': 3000,
    '3001/tcp': 3001
}

crearContenedor(descargarImagen('lscr.io/linuxserver/webtop'), 'webtop', puertos=webtopPorts)
detenerContenedor('webtop')
ejecutarContenedor('webtop')
#listarContenedores()