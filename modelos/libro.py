# Modelo que representa un libro en la biblioteca

class Libro:

    def __init__(self, titulo, autor, categoria, isbn):
        # título y autor almacenados como tupla (requisito)
        self.info = (titulo, autor)

        self.categoria = categoria
        self.isbn = isbn

    def obtener_titulo(self):
        return self.info[0]

    def obtener_autor(self):
        return self.info[1]

    def mostrar_info(self):
        return f"Título: {self.obtener_titulo()} | Autor: {self.obtener_autor()} | Categoría: {self.categoria} | ISBN: {self.isbn}"
