'''
Verbos regulares

La conjugación para todos los verbos regulares del español, se puede construir a partir de los verbos en infinitivo, tener en cuenta que todos los verbos en infinitivo se dividen en 3 grupos:

Terminados en ar
Terminados en er
Terminados en ir

Construir un programa que lea por consola un verbo en infinitivo y devuelva una cadena con las 6 conjugaciones del verbo.
Ejemplo:

Entrada: correr
Salida: Yo corro, tú corres, él corre, nosotros corremos, vosotros corréis, ellos corren

Entrada: pulir
Salida: Yo pulo, tu pules, él pule, nosotros pulimos, vosotros pulis, ellos pulen
https://blablaespanol.com/wp-content/uploads/2020/10/terminaciones-1024x576.png
'''

conjTexto = ""
conjugaciones = {
    #             nosotros/as   ellos/as 
    #      yo   tu       vosotros/as
    'ar' : ('o','as','amos','áis','an'),
    'er' : ('o','es','e','emos','éis','en'),
    'ir' : ('o','es','e','imos','is','em')
}
pronombres = ['yo','tú','él','nosotros','vosotros','ellos']
verbo = input("Ingrese verbo a conjugar: ")
#verbo = 'amar'
#print(verbo)
##verbo = verbo.strip()
#print(verbo)
verbo = verbo.lower()
tamanno = len(verbo)
raiz = slice(0,tamanno-2)
raiz = verbo[raiz]
terminacion = verbo[-2:]
#print(raiz+"-"+terminacion)
#print(pronombres[0])
#print(conjugaciones[terminacion][0])
for i in range((len(pronombres))-1):
    conjTexto += "¬ "+pronombres[i] + " "+ raiz + conjugaciones[terminacion][i]+".\n"
    
print("Conjugacion del verbo "+verbo+"\n"+conjTexto)