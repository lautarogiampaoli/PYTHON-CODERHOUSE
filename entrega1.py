def mostrar_menu():
    print("---- SISTEMA DE NOTAS -----")
    print("1. Agregar estudiante y nota")
    print("2. Ver todas las notas")
    print("3. Ver promedio de notas")
    print("4. Salir")
    print("==============================")

def agregar_nota(nombres, notas):
    print("\n--- Agregar estudiante ---")
    nombre = input("Nombre del estudiante: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacío.\n")
        return

    while True:
        nota_str = input("Nota (0 a 10): ").strip()
        try:
            nota = float(nota_str)
            if nota < 0 or nota > 10:
                print("La nota debe estar entre 0 y 10.")
                continue
            break
        except ValueError:
            print("Por favor, ingresa un número válido para la nota.")

    nombres.append(nombre)
    notas.append(nota)
    print(f"\n✅ Nota cargada: {nombre} - {nota}\n")

def ver_notas(nombres, notas):
    print("\n--- Listado de notas ---")
    if len(nombres) == 0:
        print("No hay notas cargadas.\n")
        return

    for i in range(len(nombres)):
        print(f"{i+1}. {nombres[i]} - {notas[i]}")
    print()

def ver_promedio(notas):
    print("\n--- Promedio de notas ---")
    if len(notas) == 0:
        print("No hay notas para calcular el promedio.\n")
        return

    suma = 0
    for n in notas:
        suma = suma + n

    promedio = suma / len(notas)
    print(f"Promedio: {promedio:.2f}\n")

def main():
    nombres = []  # lista de nombres de estudiantes
    notas = []    # lista de notas correspondientes

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ").strip()

        if opcion == "1":
            agregar_nota(nombres, notas)
        elif opcion == "2":
            ver_notas(nombres, notas)
        elif opcion == "3":
            ver_promedio(notas)
        elif opcion == "4":
            print("\nSaliendo... ¡Hasta luego!\n")
            break
        else:
            print("\nOpción inválida, intenta de nuevo.\n")

# Punto de entrada del programa
main()
