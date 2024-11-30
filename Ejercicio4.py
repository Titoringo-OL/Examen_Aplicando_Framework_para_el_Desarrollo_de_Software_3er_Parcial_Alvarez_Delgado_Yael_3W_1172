print(" ")
print("Alvarez Delgado Yael Ismael 3W 1172")
print(" ")

# Creamos la clase
class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # Método para sumar los dos números
    def suma(self):
        return self.num1 + self.num2

    # Método para restar los dos números
    def resta(self):
        return self.num1 - self.num2

    # Método para multiplicar los dos números
    def multiplicacion(self):
        return self.num1 * self.num2

    # Método para dividir los dos números
    def division(self):
        # Verificar si el segundo número es cero para evitar división por cero
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: División por cero"

# Solicitar los valores al usuario
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Crear una instancia de la clase Calculadora
calculadora = Calculadora(numero1, numero2)

# Imprimir los resultados de las operaciones
print(f"La suma de {numero1} y {numero2} es: {calculadora.suma()}")
print(f"La resta de {numero1} y {numero2} es: {calculadora.resta()}")
print(f"La multiplicación de {numero1} y {numero2} es: {calculadora.multiplicacion()}")
print(f"La división de {numero1} y {numero2} es: {calculadora.division()}")