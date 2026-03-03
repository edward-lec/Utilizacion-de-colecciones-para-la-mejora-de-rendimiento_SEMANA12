# servicios/biblioteca_servicio.py

from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:
    """
    Clase que contiene TODA la lógica del negocio.

    Decisión de arquitectura:
    - Aquí se maneja la lógica del sistema.
    - main.py SOLO ejecuta el programa.
    - modelos SOLO representan entidades.

    Colecciones utilizadas (requisitos obligatorios):

    - Diccionario para libros disponibles:
        Clave: ISBN
        Valor: Objeto Libro

    - Diccionario para usuarios:
        Clave: user_id
        Valor: Objeto Usuario

    - Set para controlar IDs únicos de usuarios.
    """

    def __init__(self):
        self.__libros_disponibles = {}  # {isbn: Libro}
        self.__usuarios = {}            # {user_id: Usuario}
        self.__ids_usuarios = set()     # Control de unicidad


    #                    LIBROS


    def agregar_libro(self, titulo, autor, categoria, isbn):
        """
        Agrega un libro al catálogo si el ISBN no existe.
        """
        if isbn in self.__libros_disponibles:
            print("El libro ya está registrado.")
            return

        libro = Libro(titulo, autor, categoria, isbn)
        self.__libros_disponibles[isbn] = libro
        print("Libro agregado correctamente.")

    def quitar_libro(self, isbn):
        """
        Elimina un libro del catálogo.
        """
        if isbn in self.__libros_disponibles:
            del self.__libros_disponibles[isbn]
            print("Libro eliminado correctamente.")
        else:
            print("Libro no encontrado.")

    #                    USUARIOS


    def registrar_usuario(self, nombre, user_id):
        """
        Registra un nuevo usuario si el ID no existe.
        """
        if user_id in self.__ids_usuarios:
            print("El ID ya está en uso.")
            return

        usuario = Usuario(nombre, user_id)
        self.__usuarios[user_id] = usuario
        self.__ids_usuarios.add(user_id)
        print("Usuario registrado correctamente.")

    def dar_baja_usuario(self, user_id):
        """
        Elimina un usuario del sistema.
        """
        if user_id in self.__usuarios:
            del self.__usuarios[user_id]
            self.__ids_usuarios.remove(user_id)
            print("Usuario eliminado correctamente.")
        else:
            print("Usuario no encontrado.")


    #                    PRÉSTAMOS


    def prestar_libro(self, user_id, isbn):
        """
        Presta un libro a un usuario:
        - Se elimina del catálogo disponible.
        - Se agrega a la lista del usuario.
        """
        if user_id not in self.__usuarios:
            print("Usuario no existe.")
            return

        if isbn not in self.__libros_disponibles:
            print("Libro no disponible.")
            return

        libro = self.__libros_disponibles.pop(isbn)
        self.__usuarios[user_id].agregar_libro(libro)

        print("Préstamo realizado correctamente.")

    def devolver_libro(self, user_id, isbn):
        """
        Devuelve un libro:
        - Se elimina de la lista del usuario.
        - Se vuelve a añadir al catálogo disponible.
        """
        if user_id not in self.__usuarios:
            print("Usuario no existe.")
            return

        libro = self.__usuarios[user_id].devolver_libro(isbn)

        if libro:
            self.__libros_disponibles[isbn] = libro
            print("Libro devuelto correctamente.")
        else:
            print("El usuario no tiene ese libro.")


    #                    BÚSQUEDAS


    def buscar_por_titulo(self, titulo):
        for libro in self.__libros_disponibles.values():
            if libro.get_titulo().lower() == titulo.lower():
                print(libro)

    def buscar_por_autor(self, autor):
        for libro in self.__libros_disponibles.values():
            if libro.get_autor().lower() == autor.lower():
                print(libro)

    def buscar_por_categoria(self, categoria):
        for libro in self.__libros_disponibles.values():
            if libro.get_categoria().lower() == categoria.lower():
                print(libro)


    #                    LISTADO


    def listar_libros_usuario(self, user_id):
        if user_id not in self.__usuarios:
            print("Usuario no existe.")
            return

        libros = self.__usuarios[user_id].get_libros_prestados()

        if not libros:
            print("No tiene libros prestados.")
            return

        for libro in libros:
            print(libro)