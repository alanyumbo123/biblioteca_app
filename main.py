# Punto de entrada del programa

from servicios.biblioteca_servicio import BibliotecaServicio

biblioteca = BibliotecaServicio()

while True:

    print("\n===== SISTEMA BIBLIOTECA DIGITAL =====")
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro por título")
    print("8. Buscar libro por autor")
    print("9. Buscar libro por categoría")
    print("10. Listar libros prestados a un usuario")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        titulo = input("Título: ")
        autor = input("Autor: ")
        categoria = input("Categoría: ")
        isbn = input("ISBN: ")

        biblioteca.agregar_libro(titulo, autor, categoria, isbn)

    elif opcion == "2":

        isbn = input("ISBN del libro a eliminar: ")
        biblioteca.quitar_libro(isbn)

    elif opcion == "3":

        nombre = input("Nombre del usuario: ")
        user_id = input("ID del usuario: ")
        biblioteca.registrar_usuario(nombre, user_id)

    elif opcion == "4":

        user_id = input("ID del usuario a eliminar: ")
        biblioteca.eliminar_usuario(user_id)

    elif opcion == "5":

        user_id = input("ID del usuario: ")
        isbn = input("ISBN del libro: ")
        biblioteca.prestar_libro(user_id, isbn)

    elif opcion == "6":

        user_id = input("ID del usuario: ")
        isbn = input("ISBN del libro: ")
        biblioteca.devolver_libro(user_id, isbn)

    elif opcion == "7":

        titulo = input("Título a buscar: ")
        biblioteca.buscar_titulo(titulo)

    elif opcion == "8":

        autor = input("Autor a buscar: ")
        biblioteca.buscar_autor(autor)

    elif opcion == "9":

        categoria = input("Categoría a buscar: ")
        biblioteca.buscar_categoria(categoria)

    elif opcion == "10":

        user_id = input("ID del usuario: ")

        if user_id in biblioteca.usuarios:
            biblioteca.usuarios[user_id].listar_libros()
        else:
            print("Usuario no encontrado.")

    elif opcion == "0":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")
