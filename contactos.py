opcion = 1

contactos = []

while opcion !=0:

    print('Selecciona una opción:')
    print('1. Crear un contacto')
    print('2. Listar los contactos')
    print('3. Actualizar contactos')
    print('4. Eliminar un contacto') 
    print('0. Salir') 

    opcion = int(input())

    if opcion == 1:
        nombre = input('Ingrese el nombre del contacto: ')
        apellido = input('Ingrese el apellido del contacto: ')
        celular = input('Ingrese el celular del contacto: ')
        correo = input('Ingrese el correo del contacto: ')

        #.append es para agresar en lo ultimo de la lista
        contactos.append({
            'nombre': nombre,
            'apellido': apellido,
            'celular': celular,
            'correo': correo,

        })

        input('Contacto guardado correctamente. Presione enter para continuar')
    elif opcion ==2:
        print(contactos)

    