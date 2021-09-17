'''
    int
    float
    str
    list => array mutable
    tupl => array inmutable
    dict => objeto
    
'''

numero1 = 10 = int
numero2 = 15.5 = float
nombre = 'Eduard' #str-->string

#Listas o arreglos => []
materias = ['Base de datos ll', 'Lenguaje de 4 generación']

listaNumeros = [0,1,2,3,4,5,6]
matrizEjemplo = [[1,2], [3,4]]

materias[0] = 'Programación avanzada'

print(materias[0])
print(matrizEjemplo[1][0])

print(materias[0], materias[1])
print(matrizEjemplo)

listaSinOrdenar = [10,15,2,-5,35]
print(listaSinOrdenar)

listaOrdenada = listaSinOrdenar.sort(reverse=true)
print(listaOrdenada)



#tuplas ==> lista inmutable => ()

#dias = ('lunes', 'martes', 'miercoles', 'jueves', 'viernes')

#print(dias[2])


#Boolean

#esCorrecto = True
#esCorrecto = False

#print(len(materias))

#print(len(dias))

#print(dias.cout('lunes'))

#Dictionary ==> {}Cuando hallan llaves posiblemente sea un diccionario

persona = {
    'nombre': 'Eduardo',
    'apellido': 'Plata',
    'edad': '35',
    'materias': ['Base de datos', 'Lenguaje de cuarta'],
    'direccion': {
        'direccion': 'barrio centro',
        'ciudad': 'Mocoa',
        'pais': 'Colombia'
    }
}

persona['apellido'] = 'Perez'

print(persona['apellido'])
print(persona['materias'][1])
print(persona['direccion']['pais'])
persona['nombre_completo'] = persona['nombre'] + ' ' + persona['apellido']
print(persona)


#Ciclos For
#cICLO FOR In
'''
for materia in materias:
    print('ESte codigo pertenence al ciclo')
    print('ESte codigo tambien pertenence al ciclo')
    print(materia)
print('Este codigo no pertenece al ciclo')
'''

#Operadores aritmeticos
'''
    + 
    - 
    * 
    /
    %
    **
'''

'''
Operadores logicos
    and
    or
    not

'''

'''
Operadores relacionales
    <
    >
    ==
    >=
    <=
    !=
'''

if 10 < 20 and 5 < 18 :
    print('Se cumple la condicion')
elif 5 < 21:
    print('Se cumple el elif')
elif 6 > 2:
    print('Se cumple el segundi elif')
else:
    print('La condicion no Se cumplio')


#Input

print('Como te llamas?')
nombre = input()

print('Bienvenido', nombre)








'''






