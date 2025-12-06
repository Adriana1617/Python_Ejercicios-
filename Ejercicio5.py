 #5 Área de un poligono 
"""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.

"""

from abc import ABC, abstractmethod

class Polygon(ABC): 
  
  def area(self):
    pass

  def print_area(self):
    print (f"El area es {self.area()}")


class Triangle(Polygon): 
  def __init__(self, base, height) :
    self.base = base
    self.height = height
    
  def area(self):
    return (self.base * self.height)/2

  def print_area(self):
    print(f"El area es {self.area()}")


class Rectangulo(Polygon): 
  def __init__(self, lenght, width):
    self.lenght = lenght
    self.width = width
  
  def area(self):
    return self.lenght * self.width
  
  def print_area(self):
    print (f"El area es {self.area()}")

    

class Square(Polygon): 
  def __init__(self, side):
    self.side = side

  def area(self):
    return self.side *self.side
  
  def print_area(self):
    print(f"El area es {self.area()}")



def Area(polygon: Polygon):
  polygon.print_area()



Area(Square(2))
