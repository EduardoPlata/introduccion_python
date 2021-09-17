'''
    Crear un programa, que lea por consola una cadena de numeros, el programa debera devolver el resultado de la multiplicacion.
    Nota: No se puede utilizar el operador de multiplicacion (*), no se puede utilizar la funcion eval. No se puede utilizar librerias.
    2*3*4

'''

cadenaNumeros = input("Ingrese cadena de numeros: ")
cadenaNumero = (cadenaNumeros.split("*"))
dato = []
datoIn = 0
def multiplicacion(a,b):
    producto = 0
    while b!=0:
        producto = producto+a
        b=b-1
    ##print(producto)
    return producto

for numero in cadenaNumero:
    dato.append(int(numero))
rango = len(dato)-1
for i in range(rango):
    if i<= rango:
        if i==0:
            datoIn= multiplicacion(dato[i], dato[i+1])
        else:
            datoIn= multiplicacion(datoIn, dato[i+1])
print("El resultado de la cadena "+cadenaNumeros+" es: "+str(datoIn))
    

