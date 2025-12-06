 #3 La sucecion Fibonacci 
"""
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""


fibonacci = []

for i in range(0,50):
  if(i == 0): 
    fibonacci.insert(i,i)
  elif (i == 1):
    fibonacci.insert(i,i)
  else: 
    fibonacci.insert(i, (fibonacci[i-1] + fibonacci[i -2]) )

print(fibonacci)
 
