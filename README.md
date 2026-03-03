**Introducción**

El presente proyecto consiste en el desarrollo de un Sistema de Gestión de Biblioteca Digital, aplicando los principios de la Programación Orientada a Objetos (POO) y una arquitectura estructurada por capas.

El objetivo principal es diseñar un sistema organizado y modular que permita gestionar libros, usuarios y préstamos, separando claramente la lógica del negocio de la ejecución del programa.

Para ello, se implementó una estructura dividida en tres capas fundamentales:

Modelos, que representan las entidades del sistema.

Servicios, que contienen la lógica del negocio.

Punto de entrada (main), encargado únicamente de la interacción con el usuario.

Además, se utilizaron diferentes estructuras de datos como tuplas, listas, diccionarios y conjuntos, cumpliendo con los requisitos técnicos establecidos.

**Desarrollo**

El sistema fue desarrollado siguiendo una arquitectura por capas que permite una mejor organización del código y facilita su mantenimiento.

En la carpeta modelos, se implementaron las clases Libro y Usuario.
La clase Libro almacena el título y autor en una tupla para garantizar la inmutabilidad de estos datos, además de incluir la categoría y el ISBN como identificador único.
La clase Usuario contiene el nombre, un ID único y una lista que gestiona los libros actualmente prestados.

En la carpeta servicios, se desarrolló la clase BibliotecaServicio, que centraliza toda la lógica del negocio. Esta clase administra:

Un diccionario para almacenar los libros disponibles, usando el ISBN como clave.

Un diccionario para los usuarios registrados.

Un conjunto (set) para garantizar la unicidad de los IDs de usuario.

La gestión de préstamos y devoluciones.

Se implementaron funcionalidades como:

Añadir y eliminar libros.

Registrar y dar de baja usuarios.

Prestar y devolver libros.

Buscar libros por título, autor y categoría.

Listar libros prestados a un usuario.

Finalmente, en el archivo main.py, se implementó un menú interactivo en consola que permite probar todas las funcionalidades del sistema, manteniendo la separación adecuada entre la interfaz y la lógica interna.

**Conclusión**

El desarrollo de este sistema permitió aplicar de manera práctica los conceptos fundamentales de la Programación Orientada a Objetos, tales como encapsulamiento, organización modular y separación de responsabilidades.

La arquitectura por capas implementada mejora la claridad del código, facilita su mantenimiento y permite futuras ampliaciones del sistema sin afectar su estructura principal.

Asimismo, el uso adecuado de colecciones como tuplas, listas, diccionarios y conjuntos demostró la importancia de seleccionar la estructura de datos correcta según la necesidad del sistema.

En conclusión, el proyecto cumple con los requisitos planteados y representa una implementación funcional y organizada de un sistema de gestión de biblioteca digital.
