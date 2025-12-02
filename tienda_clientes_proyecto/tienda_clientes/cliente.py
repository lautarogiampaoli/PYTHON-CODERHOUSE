# tienda_clientes/cliente.py

from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class Cliente:
    """Clase que modela un cliente de una página de compras."""

    # Atributo de clase para contar cuántos clientes se han creado
    contador_clientes: ClassVar[int] = 0

    # Atributos de instancia
    id_cliente: int = field(init=False)
    nombre: str
    email: str
    direccion: str
    saldo: float = 0.0
    activo: bool = True

    def __post_init__(self):
        """Se ejecuta luego del __init__ generado por dataclass."""
        type(self).contador_clientes += 1
        self.id_cliente = type(self).contador_clientes

    def __str__(self) -> str:
        """Representación legible para los objetos Cliente."""
        estado = "Activo" if self.activo else "Inactivo"
        return (f"Cliente #{self.id_cliente} - {self.nombre} "
                f"({self.email}) - Saldo: ${self.saldo:.2f} - {estado}")

    # ===== Métodos "normales" (no magic) =====

    def actualizar_direccion(self, nueva_direccion: str) -> None:
        """Actualiza la dirección del cliente."""
        if not nueva_direccion.strip():
            raise ValueError("La nueva dirección no puede estar vacía.")
        self.direccion = nueva_direccion

    def registrar_compra(self, monto: float) -> None:
        """Registra una compra restando el monto al saldo disponible."""
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a 0.")
        if monto > self.saldo:
            raise ValueError("Saldo insuficiente para registrar la compra.")
        self.saldo -= monto

    def recargar_saldo(self, monto: float) -> None:
        """Recarga el saldo del cliente (por ejemplo, carga de crédito)."""
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a 0.")
        self.saldo += monto

    def desactivar(self) -> None:
        """Marca el cliente como inactivo."""
        self.activo = False

    def activar(self) -> None:
        """Marca el cliente como activo."""
        self.activo = True
