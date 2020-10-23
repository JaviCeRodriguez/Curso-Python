class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangulo(Punto):
    def __init__(self, Punto1, Punto2):
        self.Punto1 = Punto1
        self.Punto2 = Punto2

    def base(self):
        return abs(self.Punto1.x - self.Punto2.x)
    
#     def altura(self):
#         return abs(self.y1 - self.y2)

#     def area(self):
#         return self.base() * self.altura()

#     def __str__(self):
#         return f'Punto 1 = ({self.x1, self.y1} y Punto 2 = ({self.x2, self.y2}))'

#     def __repr__(self):
#         return f'Punto({self.x1}, {self.y1}, {self.x2}, {self.y2})'

# puntos = Rectangulo(2, 4, 1, 8)
# print(f'Punto 1 = ({puntos.x1}, {puntos.y1})\nPunto 2 = ({puntos.x2}, {puntos.y2})')
# print(f'Base = {puntos.base()}')
# print(f'Altura = {puntos.altura()}')
# print(f'Area = {puntos.area()}')
# print(puntos.__str__())
# print(puntos.__repr__())

#     # def desplazar(self, desplazamiento):
    
#     # def rotar(self):

    