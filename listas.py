#Listas o arreglos

miLista = [1,2,3,4,5,6,7,"hola",3.8]
print(miLista[8])

#Para acceder a una posición lo hacemos: miLista[index]

#append

print(miLista)
miLista.append("python")
print(miLista)

#insert
miLista.insert(0, "JavaScript")
print(miLista)

#Reasignar o modificar
miLista[0] = "HTML"
miLista[3] = "CSS"
print(miLista)

#Para eliminar utilizar "del"
del miLista[4]
print(miLista)

#Para elimianr utilizar "remove"
miLista.append("CSS")
miLista.remove("CSS")
print(miLista)

#len: cantidad de elementos en una lista
print(len(miLista))

