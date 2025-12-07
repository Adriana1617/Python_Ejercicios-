#9 Decimal a Binario 

"""
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""

def Binario(decimal): 
  binario = ""

  while decimal != 0: 
     mod = str(decimal % 2)
     binario = mod + binario
     decimal = decimal // 2
  return binario  

print(Binario(29))
