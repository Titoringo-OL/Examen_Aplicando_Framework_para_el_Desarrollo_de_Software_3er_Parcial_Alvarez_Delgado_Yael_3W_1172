print(" ")
print("Alvarez Delgado Yael Ismael 3W 1172")
print(" ")

# Creamos la clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Pedimos sus datos al usuario
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

    # Comprobamos que sea mayor de edad
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} no es mayor de edad.")
            
# Ejemplo de una persona mayor de edad
persona1 = Persona("Tony", 25)
persona1.mostrar_datos()
persona1.es_mayor_de_edad()

# Ejemplo de una persona menor de edad
persona2 = Persona("Alixa", 16)
persona2.mostrar_datos()
persona2.es_mayor_de_edad()