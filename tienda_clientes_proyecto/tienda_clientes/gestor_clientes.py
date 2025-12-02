# tienda_clientes/gestor_clientes.py

from typing import List, Optional
from .cliente import Cliente


class GestorClientes:
    """Clase que gestiona una colección de clientes."""

    def __init__(self):
        self._clientes: List[Cliente] = []

    def agregar_cliente(self, cliente: Cliente) -> None:
        """Agrega un cliente al gestor."""
        self._clientes.append(cliente)

    def buscar_por_email(self, email: str) -> Optional[Cliente]:
        """Devuelve el cliente cuyo email coincida (o None si no lo encuentra)."""
        for cliente in self._clientes:
            if cliente.email.lower() == email.lower():
                return cliente
        return None

    def listar_activos(self) -> List[Cliente]:
        """Devuelve una lista con los clientes activos."""
        return [c for c in self._clientes if c.activo]

    def listar_todos(self) -> List[Cliente]:
        """Devuelve todos los clientes (activos e inactivos)."""
        return list(self._clientes)

    def eliminar_cliente(self, id_cliente: int) -> bool:
        """Elimina un cliente por id. Devuelve True si lo encontró y eliminó."""
        for i, cliente in enumerate(self._clientes):
            if cliente.id_cliente == id_cliente:
                del self._clientes[i]
                return True
        return False
