import json

def cargar_inventario():
    try:
        with open("inventario.json", "r") as archivo:
            data = json.load(archivo)
            if isinstance(data, dict):
                return data
            else:
                print("⚠️ Archivo inventario.json corrupto, reiniciando inventario...")
                return {}
    except FileNotFoundError:
        return {}

def guardar_inventario(inventario):
    with open("inventario.json", "w") as archivo:
        json.dump(inventario, archivo, indent=4)

def registrar_producto(inventario):
    nombre = input("\nNombre del producto: ").capitalize()
    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("Error: Debes ingresar números válidos para precio y cantidad.")
        return 

    if nombre in inventario:
        inventario[nombre]["cantidad"] += cantidad
    else:
        inventario[nombre] = {"precio": precio, "cantidad": cantidad}

    guardar_inventario(inventario)
    print(f"Producto '{nombre}' registrado/actualizado correctamente.")

def listar_productos(inventario):
    if not inventario:
        print("Inventario vacío.")
    else:
        print("\n--- INVENTARIO ---")
        for nombre, datos in inventario.items():
            print(f"{nombre} → Precio: {datos['precio']} | Cantidad: {datos['cantidad']}")

def actualizar_cantidad(inventario):
    nombre = input("\nNombre del producto a actualizar: ")
    if nombre in inventario:
        try:
            nueva_cantidad = int(input("Nueva cantidad: "))
        except ValueError:
            print("Error: La cantidad debe ser un número entero.")
            return
        inventario[nombre]["cantidad"] = nueva_cantidad
        guardar_inventario(inventario)
        print(f"Cantidad de '{nombre}' actualizada correctamente.")
    else:
        print("El producto no existe en el inventario.")

def eliminar_producto(inventario):
    nombre = input("\nNombre del producto a eliminar: ")
    if nombre in inventario:
        del inventario[nombre]
        guardar_inventario(inventario)
        print(f"Producto '{nombre}' eliminado correctamente.")
    else:
        print("El producto no existe en el inventario.")

def calcular_valor_total(inventario):
    if not inventario:
        print("Inventario vacío.")
    else:
        total = sum(datos["precio"] * datos["cantidad"] for datos in inventario.values())
        print(f"Valor total del inventario: {total}")

def main():
    inventario = cargar_inventario()

    while True:
        print("\n--- MENÚ ---\n")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Actualizar cantidad")
        print("4. Eliminar producto")
        print("5. Calcular valor total del inventario")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        try:
            if opcion == "1":
                registrar_producto(inventario)
            elif opcion == "2":
                listar_productos(inventario)
            elif opcion == "3":
                actualizar_cantidad(inventario)
            elif opcion == "4":
                eliminar_producto(inventario)
            elif opcion == "5":
                calcular_valor_total(inventario)
            elif opcion == "6":
                break
            else:
                print("Opción no válida.")
        except Exception as e:
            print(f"Error: {e}")


main()