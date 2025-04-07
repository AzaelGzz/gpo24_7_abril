class Cuadrado:
    def __init__(self,lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado **2
    
cuadrado = Cuadrado(5)
print(cuadrado.calcular_area())
