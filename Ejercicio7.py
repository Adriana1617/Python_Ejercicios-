 #7 Invirtiendo cadenas
"""
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""


def InvetirCadena(word):
  listw = []
  for w in word: 
    listw.append(w)

  listw.reverse()
  newword = "".join(listw)
  print(newword)

  
InvetirCadena("Hola Mundo")


"""
"""

def InvetirCadena(word):
 newList = []
 posicion = 1
 
 for i in range(len(word), 0,-1):
   for w in word:
     if (posicion == i): 
        newList.append(w)
        posicion = 1
        break
     else:
        posicion += 1
         
 cadena = "".join(newList)
 print(cadena)
InvetirCadena("Hola Mundo")


"""
"""


def invertir_cadena(word):
    nueva = ""
    for letra in word:
        nueva = letra + nueva   # agrega la letra al inicio
    return nueva

print(invertir_cadena("Hola Mundo"))
