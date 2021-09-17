from hashlib import md5
from validaciones import Validaciones
from archivo import Archivo

archivoUsuarios = Archivo('usuarios.json')

archivoAnimales = Archivo('animales.json')

usuarios = []

class Usuarios:
    id = 1 

    def agregar(self):
        nombres = input("Ingresa los nombres del usuario: ")

        while not Validaciones.requerido(nombres):
            nombres = input("Ingresa los nombres del usuario: ")

        apellidos = input("Ingresa los apellidos del usuario: ")

        while not Validaciones.requerido(apellidos):
            apellidos = input("Ingresa los apellidos del usuario: ")

        celular = input("Ingresa el celular del usuario: ")

        email = input("Ingresa el email del usuario: ")

        while not Validaciones.requerido(email) or not Validaciones.email(email):
            email = input("Ingresa el email del usuario: ")

        contrasena = input("Ingresa la contraseña del usuario: ")

        usuarios.append({
            "id": self.id,
            "nombres": nombres,
            "apellidos": apellidos,
            "celular": celular,
            "email": email,
            "contrasena": md5(contrasena.encode("utf-8")).hexdigest(),
        })
        self.id += 1
        archivoUsuarios.escribir(usuarios)
        archivoAnimales.escribir(usuarios)
        print("El usuario", nombres, "se ha agregado correctamente")

    def listar(self):
        if(not len(usuarios)):
            print("No se han encontrado registros")
        else:
            print("Listado de usuarios")
            print("____________________________")
            print("ID|Nombres|Apellidos|Celular|Email|Contraseña")
            for usuario in usuarios:
                print(usuario["id"],"|",usuario["nombres"],"|",usuario["apellidos"],"|",usuario["celular"], "|", usuario["email"], "|", usuario["contrasena"])
            print("____________________________")
    
    def editar(self):
        usuario_eliminar = int(input("Ingrese el id del usuario a editar: "))
        index_eliminar = -1
        usuario = {}
        for index, persona in enumerate(usuarios):
            if(usuario_eliminar == persona["id"]):
                index_eliminar = index
                usuario = persona

        if(index_eliminar == -1):
            print("No se ha encontrado ningun usuario con el id", usuario_eliminar)
        else:
            print("Actualizando datos del usuario", usuario['nombres'],", dejar los campos en blanco si no desea cambiar la información")
            nombres = input("Nombres (" + usuario['nombres'] + "): ")
            apellidos = input("Apellidos (" + usuario['apellidos'] + "): ")
            celular = input("Celular (" + usuario['celular'] + "): ")

            if(nombres != ""):
                usuario['nombres'] = nombres
            
            if(apellidos != ""):
                usuario['apellidos'] = apellidos

            if(celular != ""):
                usuario['celular'] = celular

            usuarios[index_eliminar] = usuario
            print("El usuario", usuario['nombres'], "ha sido actualizado correctamente")

    def eliminar(self):
        usuario_eliminar = int(input("Ingrese el id del usuario a eliminar: "))
        index_eliminar = -1
        usuario = {}
        for index, persona in enumerate(usuarios):
            if(usuario_eliminar == persona["id"]):
                index_eliminar = index
                usuario = persona

        if(index_eliminar == -1):
            print("No se ha encontrado ningun usuario con el id", usuario_eliminar)
        else:
            del usuarios[index_eliminar]
            print("El usuario", usuario['nombres'], "se ha eliminado correctamente")

    def login(self):
        email = input("Email: ")
        password = input("Contraseña: ")

        password = md5(password.encode("utf-8")).hexdigest()

        for usuario in usuarios:
            if usuario["email"] == email and usuario["contrasena"] == password:
                print("Login correcto")
