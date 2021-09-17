import json

class Archivo:
    ruta = 'usuarios.json'

    def __init__(self, ruta):
        self.ruta = ruta

    def leer(self):
        archivo = open(self.ruta, 'r')
        usuarios = archivo.read()
        usuarios = json.loads(usuarios)
        archivo.close()
        return usuarios

    def escribir(self, nuevos_usuarios):
        archivo = open(self.ruta, 'w')
        archivo.write(json.dumps(nuevos_usuarios))
        archivo.close()