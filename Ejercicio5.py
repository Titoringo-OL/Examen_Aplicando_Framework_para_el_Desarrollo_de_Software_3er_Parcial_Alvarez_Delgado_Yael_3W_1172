print(" ")
print("Alvarez Delgado Yael Ismael 3W 1172")
print(" ")

# Creams la clase
class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"


class Agenda:
    def __init__(self):
        self.contactos = []

    # Método para añadir un contacto
    def añadir_contacto(self):
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        email = input("Ingrese el email del contacto: ")
        nuevo_contacto = Contacto(nombre, telefono, email)
        self.contactos.append(nuevo_contacto)
        print("Contacto añadido exitosamente.")

    # Método para mostrar todos los contactos
    def lista_contactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
        else:
            print("Lista de contactos:")
            for contacto in self.contactos:
                print(contacto)

    # Método para buscar un contacto por nombre
    def buscar_contacto(self):
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        encontrado = False
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print("Contacto encontrado:")
                print(contacto)
                encontrado = True
                break
        if not encontrado:
            print(f"No se encontró ningún contacto con el nombre {nombre}.")

    # Método para editar un contacto
    def editar_contacto(self):
        nombre = input("Ingrese el nombre del contacto a editar: ")
        encontrado = False
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print(f"Contacto encontrado: {contacto}")
                print("Ingrese los nuevos datos.")
                contacto.nombre = input("Nuevo nombre: ")
                contacto.telefono = input("Nuevo teléfono: ")
                contacto.email = input("Nuevo email: ")
                print("Contacto editado exitosamente.")
                encontrado = True
                break
        if not encontrado:
            print(f"No se encontró ningún contacto con el nombre {nombre}.")

    # Método para cerrar la agenda
    def cerrar_agenda(self):
        print("Cerrando la agenda. ¡Hasta luego!")
        exit()


def mostrar_menu():
    print("\nAgenda de contactos:")
    print("1. Añadir contacto")
    print("2. Lista de contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Cerrar agenda")
    opcion = input("Seleccione una opción: ")
    return opcion


def ejecutar_agenda():
    agenda = Agenda()

    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            agenda.añadir_contacto()
        elif opcion == '2':
            agenda.lista_contactos()
        elif opcion == '3':
            agenda.buscar_contacto()
        elif opcion == '4':
            agenda.editar_contacto()
        elif opcion == '5':
            agenda.cerrar_agenda()
        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecutar la agenda
ejecutar_agenda()
