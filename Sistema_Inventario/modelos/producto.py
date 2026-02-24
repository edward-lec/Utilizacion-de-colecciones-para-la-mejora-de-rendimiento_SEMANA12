# modelos/producto.py

class Producto:
    """
    Clase que representa un producto dentro del inventario.

    Atributos:
        __id (str): Identificador único del producto.
        __nombre (str): Nombre del producto.
        __cantidad (int): Cantidad disponible en stock.
        __precio (float): Precio unitario del producto.
    """

    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
        # Encapsulamiento: atributos privados
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio


    # Métodos GETTERS


    def get_id(self) -> str:
        return self.__id

    def get_nombre(self) -> str:
        return self.__nombre

    def get_cantidad(self) -> int:
        return self.__cantidad

    def get_precio(self) -> float:
        return self.__precio


    # Métodos SETTERS


    def set_nombre(self, nombre: str):
        self.__nombre = nombre

    def set_cantidad(self, cantidad: int):
        self.__cantidad = cantidad

    def set_precio(self, precio: float):
        self.__precio = precio


    # Métodos de Serialización


    def to_dict(self) -> dict:
        """
        Convierte el objeto Producto en un diccionario
        para poder almacenarlo en formato JSON.
        """
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "precio": self.__precio
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Crea un objeto Producto a partir de un diccionario.
        """
        return Producto(
            data["id"],
            data["nombre"],
            data["cantidad"],
            data["precio"]
        )