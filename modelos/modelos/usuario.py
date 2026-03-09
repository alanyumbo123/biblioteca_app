# Modelo que representa un usuario de la biblioteca

class Usuario:

    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id

        # lista de libros prestados
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        for libro in self.libros_prestados:
            if libro.isbn == isbn:
                self.libros_prestados.remove(libro)
                return libro
        return None

    def listar_libros(self):
        if not self.libros_prestados:
            print("El usuario no tiene libros prestados.")
        else:
            for libro in self.libros_prestados:
                print(libro.mostrar_info())
