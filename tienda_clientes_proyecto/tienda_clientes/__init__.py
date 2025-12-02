# tienda_clientes/__init__.py

"""Paquete tienda_clientes.

Permite modelar clientes de una página de compras y gestionar una colección de ellos.
"""

from .cliente import Cliente
from .gestor_clientes import GestorClientes

__all__ = ["Cliente", "GestorClientes"]
