'''
Realizar un programa, que tenga como entrada una cadena de caracteres 
El programa me debe determinar la cantidad de veces que se repite todas
las letras

Ejemplo:

Entrada: Esta lloviendo
Salida: e:2  s:1  t:1  a:1  l:2  o:2  v:1  i:1  n:1  d:1   

'''

texto = 'esta lloviendo'

letrasUnicas = []

for letra in texto:
    cont = 0

    for letraUnica in letrasUnicas:
        if letraUnica == letra:
            cont += 1

    if cont == 0:
        letrasUnicas.append(letra)

for letraUnica in letrasUnicas:
    print(letraUnica, texto.count(letraUnica))



    '''resultado = {}

for letra in texto:
    if resultado.get(letra):
        resultado[letra] += 1
    else:
        resultado[letra] = 1    
print(resultado)

'''



 
