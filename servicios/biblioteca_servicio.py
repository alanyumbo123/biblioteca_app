# Servicio que maneja la lógica del sistema

from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:

    def __init__(self):

        # diccionario de libros disponibles
        self.libros = {}

        # usuarios registrados
        self.usuarios = {}

        # conjunto para controlar ids únicos
        self.ids_usuarios = set()

    # añadir libro
    def agregar_libro(self, titulo, autor, categoria, isbn):
        if isbn in self.libros:
            print("El libro ya existe.")
            return

        libro = Libro(titulo, autor, categoria, isbn)
        self.libros[isbn] = libro
        print("Libro añadido correctamente.")

    # quitar libro
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    # registrar usuario
    def registrar_usuario(self, nombre, user_id):

        if user_id in self.ids_usuarios:
            print("El ID ya existe.")
            return

        usuario = Usuario(nombre, user_id)
        self.usuarios[user_id] = usuario
        self.ids_usuarios.add(user_id)

        print("Usuario registrado.")

    # eliminar usuario
    def eliminar_usuario(self, user_id):

        if user_id in self.usuarios:
            del self.usuarios[user_id]
            self.ids_usuarios.remove(user_id)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # prestar libro
    def prestar_libro(self, user_id, isbn):

        if user_id not in self.usuarios:
            print("Usuario no existe.")
            return

        if isbn not in self.libros:
            print("Libro no disponible.")
            return

        usuario = self.usuarios[user_id]
        libro = self.libros.pop(isbn)

        usuario.prestar_libro(libro)

        print("Libro prestado.")

    # devolver libro
    def devolver_libro(self, user_id, isbn):

        usuario = self.usuarios.get(user_id)

        if not usuario:
            print("Usuario no encontrado.")
            return

        libro = usuario.devolver_libro(isbn)

        if libro:
            self.libros[isbn] = libro
            print("Libro devuelto.")
        else:
            print("Ese libro no estaba prestado.")

    # buscar libro por titulo
    def buscar_titulo(self, titulo):

        for libro in self.libros.values():
            if libro.obtener_titulo().lower() == titulo.lower():
                print(libro.mostrar_info())

    # buscar por autor
    def buscar_autor(self, autor):

        for libro in self.libros.values():
            if libro.obtener_autor().lower() == autor.lower():
                print(libro.mostrar_info())

    # buscar por categoria
    def buscar_categoria(self, categoria):

        for libro in self.libros.values():
            if libro.categoria.lower() == categoria.lower():
                print(libro.mostrar_info())
