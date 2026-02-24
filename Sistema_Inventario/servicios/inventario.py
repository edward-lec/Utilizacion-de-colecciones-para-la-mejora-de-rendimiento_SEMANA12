# servicios/inventario.py

import json
import os
from modelos.producto import Producto


class Inventario:
    """
    Clase encargada de gestionar los productos.

    Utiliza un diccionario como estructura principal:
        Clave: ID del producto
        Valor: Objeto Producto

    Esto permite:
        Búsqueda rápida O(1)
        Eliminación eficiente
        Actualización directa
    """

    def __init__(self):
        # Colección principal (diccionario)
        self.productos: dict[str, Producto] = {}



    # CRUD DEL INVENTARIO


    def agregar_producto(self, producto: Producto):
        """
        Agrega un nuevo producto al inventario.
        """
        if producto.get_id() in self.productos:
            print("❌ Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.get_id()] = producto
            print("✅ Producto agregado correctamente.")


    def eliminar_producto(self, id_producto: str):
        """
        Elimina un producto usando su ID.
        """
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("🗑️ Producto eliminado correctamente.")
        else:
            print("❌ Producto no encontrado.")


    def actualizar_producto(self, id_producto: str, cantidad=None, precio=None):
        """
        Actualiza la cantidad o el precio de un producto.
        """
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)

            if precio is not None:
                self.productos[id_producto].set_precio(precio)

            print("🔄 Producto actualizado correctamente.")
        else:
            print("❌ Producto no encontrado.")


    def buscar_por_nombre(self, nombre: str):
        """
        Busca productos por coincidencia en el nombre.
        Utiliza lista por comprensión.
        """

        # LISTA
        resultados = [
            producto for producto in self.productos.values()
            if nombre.lower() in producto.get_nombre().lower()
        ]

        if resultados:
            for producto in resultados:
                self.mostrar_producto(producto)
        else:
            print("🔍 No se encontraron productos.")


    def mostrar_producto(self, producto: Producto):
        """
        Muestra la información de un producto.
        """
        print(f"ID: {producto.get_id()}")
        print(f"Nombre: {producto.get_nombre()}")
        print(f"Cantidad: {producto.get_cantidad()}")
        print(f"Precio: ${producto.get_precio():.2f}")
        print("-" * 30)


    def mostrar_todos(self):
        """
        Muestra todos los productos del inventario.
        """
        if not self.productos:
            print("📭 Inventario vacío.")
        else:
            for producto in self.productos.values():
                self.mostrar_producto(producto)



    # COLECCIONES ADICIONALES


    def obtener_ids(self):
        """
        Devuelve los IDs de productos usando un CONJUNTO (set).
        """
        return set(self.productos.keys())


    def resumen_inventario(self):
        """
        Devuelve un resumen del inventario usando una TUPLA (tuple).
        (total_productos, cantidad_total)
        """

        total_productos = len(self.productos)

        total_cantidad = sum(
            producto.get_cantidad()
            for producto in self.productos.values()
        )

        return (total_productos, total_cantidad)



    # PERSISTENCIA (ARCHIVOS)


    def guardar_archivo(self, ruta="datos/inventario.json"):
        """
        Guarda el inventario en formato JSON.
        """

        os.makedirs("datos", exist_ok=True)

        with open(ruta, "w", encoding="utf-8") as archivo:

            json.dump(
                {id_p: p.to_dict() for id_p, p in self.productos.items()},
                archivo,
                indent=4
            )

        print("💾 Inventario guardado correctamente.")


    def cargar_archivo(self, ruta="datos/inventario.json"):
        """
        Carga el inventario desde un archivo JSON.
        """

        if not os.path.exists(ruta):
            print("⚠️ No existe archivo previo de inventario.")
            return

        with open(ruta, "r", encoding="utf-8") as archivo:

            datos = json.load(archivo)

            for id_p, info in datos.items():
                self.productos[id_p] = Producto.from_dict(info)

        print("📂 Inventario cargado correctamente.")