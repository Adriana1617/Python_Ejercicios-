 #8 Contando palabras 
"""
* Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
"""

import re

def Contador(cadena_original):
  cadena_original = cadena_original.lower()
  cadena_limpia = re.sub(r'[^a-z0-9\s]', '', cadena_original)
  cadena_sin_espacios = re.sub(r'\s+', ' ', cadena_limpia)
  cadena_sin_espacios = cadena_sin_espacios + " "

  listpalabras = []
  palabra = ""
  contador = 0 
  diccionario = {}
  
  for l in cadena_sin_espacios: 
    if(l == " "):
      listpalabras.append(palabra) 
      palabra = ""
    else: 
      palabra = palabra + l 


  for i in range (len(listpalabras)):
    palabra_actual = listpalabras[i]

    if (palabra_actual in diccionario):
      continue
    contador = 0
    
    for j in range (len(listpalabras)): 

      if (palabra_actual == listpalabras[j]):
        contador += 1
    diccionario[palabra_actual] = contador

  print(diccionario)
 
      
Contador("hola Hola COMO como estas")
