import json

def agregar_producto():
    try:
        nombre = input("\nNombre del producto: ")  
        precio = int(input("\nPrecio: "))          
        cantidad = int(input("\nCantidad a agregar: "))
        
        print(f"\nProducto agregado: {nombre}, Precio: {precio}, Cantidad: {cantidad}\n")
    
    except ValueError:
        print("\nError: Debes ingresar números válidos para precio y cantidad.\n")
    except TypeError:
        print("\nError: Tipo de dato incorrecto.\n")

def eliminar_producto():
    try:
        nombre = input("\nNombre del producto a eliminar: ")
        unidad = int(input("\nCantidad a eliminar: "))
        print(f"\nProducto eliminado: {nombre}, Cantidad: {unidad}\n")
    except ValueError:
        print("\nError: Debes ingresar un nombre válido.\n")
    except TypeError:
        print("\nError: Tipo de dato incorrecto.\n")
