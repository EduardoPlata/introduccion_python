class persona:
    nombres = 'Eduard'
    apellidos = 'Plata'
    celular = '3142568756'
    email = 'eduardplatt77@otmail.com'

    def hablar(self, mensaje):
        print(mensaje)

    def guardar(self):
        print('Estamos guardando el usuario', + self.nombres, + ' ' + self.apellidos)

persona1 = persona()
persona1.guardar()

persona1.hablar('Hola mundo')

persona1.apellidos = "Perez"
persona1.nombres = "Juan"
persona1.guardar()

persona1.actualizar()

from modelos.persona import persona
from modelos.productos import producto, categorias



    