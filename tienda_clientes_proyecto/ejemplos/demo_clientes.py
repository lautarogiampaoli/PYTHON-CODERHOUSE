
from tienda_clientes import Cliente, GestorClientes


def main():
    gestor = GestorClientes()

    cliente1 = Cliente(
        nombre="Juan Pérez",
        email="juan@example.com",
        direccion="Calle Falsa 123",
        saldo=5000
    )

    cliente2 = Cliente(
        nombre="María Gómez",
        email="maria@example.com",
        direccion="Av. Siempre Viva 742",
        saldo=2000
    )


    gestor.agregar_cliente(cliente1)
    gestor.agregar_cliente(cliente2)


    print("=== Todos los clientes ===")
    for c in gestor.listar_todos():
        print(c)


    print("\n=== Registrando compra de $1500 a Juan ===")
    cliente1.registrar_compra(1500)
    print(cliente1)


    print("\n=== Actualizando dirección de María ===")
    cliente2.actualizar_direccion("Av. Libertador 9999")
    print(cliente2)


    print("\n=== Buscando cliente por email ===")
    encontrado = gestor.buscar_por_email("maria@example.com")
    if encontrado:
        print("Encontrado:", encontrado)
    else:
        print("No se encontró el cliente.")


    print("\n=== Desactivando a Juan ===")
    cliente1.desactivar()
    print(cliente1)


    print("\n=== Clientes activos ===")
    for c in gestor.listar_activos():
        print(c)


if __name__ == "__main__":
    main()
