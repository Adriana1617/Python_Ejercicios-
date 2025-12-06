#4 ¿Es un número primo?
"""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""

primos = [2]

for i in range(3,101):
  divisor = 0
  for j in range(i,1,-1):
    if(i % j == 0):
      divisor += 1
  
  if (divisor == 1):
    primos.append(i)

print(primos)
