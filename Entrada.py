nombre = input("¿Cual es tu nombre?: ")
edad = input("Hola, " + nombre + " ¿Cual es tu edad? ")
edad = int(edad)
print(nombre, "tienes", edad, "años")

if(edad < 18):
    print(nombre, "eres menor de edad")
else:
    print(nombre, "eres mayor de edad")