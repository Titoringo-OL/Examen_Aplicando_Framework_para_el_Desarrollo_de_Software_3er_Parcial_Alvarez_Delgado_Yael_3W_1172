print(" ")
print("Alvarez Delgado Yael Ismael 3W 1172")
print(" ")

# Creamos la clase
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    # Método para imprimir el valor del lado mayor
    def lado_mayor(self):
        mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado mayor es: {mayor}")

    # Método para determinar el tipo de triángulo
    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero.")
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            print("El triángulo es isósceles.")
        else:
            print("El triángulo es escaleno.")

# Ejemplos
triangulo1 = Triangulo(5, 5, 5)
triangulo1.lado_mayor()
triangulo1.tipo_triangulo()

triangulo2 = Triangulo(6, 7, 6)
triangulo2.lado_mayor()
triangulo2.tipo_triangulo()

triangulo3 = Triangulo(4, 5, 6)
triangulo3.lado_mayor()
triangulo3.tipo_triangulo()