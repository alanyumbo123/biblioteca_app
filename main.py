# Punto de entrada del programa

from servicios.biblioteca_servicio import BibliotecaServicio

biblioteca = BibliotecaServicio()

while True:

    print("\n--- SISTEMA BIBLIOTECA ---")
    print("1. Añadir libro")
    print("2. Registrar usuario")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Buscar libro por titulo")
    print("6. Salir")

    opcion = input("Seleccione opción: ")

    if opcion == "1":

        titulo = input("Título: ")
        autor = input("Autor: ")
        categoria = input("Categoría: ")
        isbn = input("ISBN: ")

        biblioteca.agregar_libro(titulo, autor, categoria, isbn)

    elif opcion == "2":

        nombre = input("Nombre usuario: ")
        user_id = input("ID usuario: ")

        biblioteca.registrar_usuario(nombre, user_id)

    elif opcion == "3":

        user_id = input("ID usuario: ")
        isbn = input("ISBN libro: ")

        biblioteca.prestar_libro(user_id, isbn)

    elif opcion == "4":

        user_id = input("ID usuario: ")
        isbn = input("ISBN libro: ")

        biblioteca.devolver_libro(user_id, isbn)

    elif opcion == "5":

        titulo = input("Título a buscar: ")
        biblioteca.buscar_titulo(titulo)

    elif opcion == "6":
        print("Saliendo del sistema...")
        break
