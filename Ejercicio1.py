print(" ")
print("Alvarez Delgado Yael Ismael 3W 1172")
print(" ")

# Creamos la clase
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

# Imprimimos los datos del alumno
    def imprimir_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

# Comprobamos si aprobo o no
    def resultado(self):
        if self.nota >= 5:
            print(f"{self.nombre} paso con un {self.nota}.")
        else:
            print(f"{self.nombre} reprobo con un {self.nota}.")

# Ejemplo de alumno aprobado
alumno1 = Alumno("Titoringo", 9.1)
alumno1.imprimir_datos()
alumno1.resultado()

# Ejemplo de alumno reprobado
alumno2 = Alumno("Werito", 4.3)
alumno2.imprimir_datos()
alumno2.resultado()

