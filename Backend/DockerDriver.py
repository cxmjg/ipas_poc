import docker

class DockerDriver:
    def __init__(self, baseUrl='tcp://127.0.0.1:2375'):
        self.client = docker.DockerClient(base_url=baseUrl)

    def descargarImagen(self, repositorio, tag='latest'):
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

    def getContenedores(self):
       return self.client.containers.list(all=True)

    def existeContenedor(self, nombre):
        try:
            self.client.containers.get(nombre)
            return True
        except docker.errors.NotFound:
            return False

    def eliminarContenedores(self):
        for contenedor in self.client.containers.list(all=True):
            contenedor.remove()
    
    def eliminarContenedor(self, nombre):
        contenedor= self.client.containers.get(nombre)
        contenedor.stop()
        contenedor.remove()

    def crearContenedor(self, imagen, nombre, comandos=None, env=None, puertos=None):
        if comandos is None:
            comandos = []
        if env is None:
            env = {}
        if puertos is None:
            puertos = {}
        return self.client.containers.create(image=imagen, command=comandos, name=nombre, ports=puertos, environment=env)

    def ejecutarContenedor(self, nombre):
        contenedor = self.client.containers.get(nombre)
        contenedor.start()
        return contenedor.status

    def detenerContenedor(self, nombre):
        contenedor = self.client.containers.get(nombre)
        contenedor.stop()
        return contenedor.status

    def reiniciarContenedor(self, nombre):
        contenedor = self.client.containers.get(nombre)
        contenedor.restart()
        return contenedor.status

    def getSalud(self, nombre):
        contenedor = self.client.containers.get(nombre)
        return contenedor.health