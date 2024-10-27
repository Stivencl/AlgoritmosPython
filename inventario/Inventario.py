class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        
def mostrar_menu():
    print("Sistema de inventario")
    print("1. Agregar producto")
    print("2. Mostrar producto")
    print("3. Buscar producto")
    print("4. Actualizar cantidad")
    print("5. eliminar producto")
    print("6. Salir")
    
inventario = []

while True:
    mostrar_menu()
    opcion = input("Elige una opción")
    
    if opcion == "6":
        print("Saliendo del programa...")
        break
    
    if opcion == "1":
        nombre = input("Digite el nombre")
        try:
            cantidad = int(input("Digite la cantidad"))
            precio = float(input("Digite el precio"))
            producto = Producto(nombre, cantidad, precio)
            inventario.append(producto)
            print("Producto agregado")
        except ValueError:
            print("Error: datos no validos")
    elif opcion == "2":
        for p in inventario:
            print(f"nombre: {p.nombre}, cantidad: {p.cantidad}, precio: {p.precio}")
    elif opcion == "3":
        nombre = input("Digite el nombre del producto a buscar")
        encontrado = False
        for p in inventario:
            if p.nombre == nombre:
                print(f"nombre: {p.nombre}, cantidad: {p.cantidad}, precio: {p.precio}")
                encontrado= True
                break
            if not encontrado:
                print("producto no encontrado")
    elif opcion == "4":
        nombre = input("Digite el nombre del producto a actualizar")
        try:
            nueva_cantidad = int(input("Ingrese la nueva cantidad"))
            for p in inventario:
                if p.nombre == nombre:
                    p.cantidad = nueva_cantidad
                    print("cantidad actualizada")
                    break
        except ValueError:
            print("Error: dato no valido")
    elif opcion == "5":
        nombre = input("Digite el nombre del producto a eliminar")
        for p in inventario:
            if p.nombre == nombre:
                inventario.remove(p)
                print("Producto eliminado")
                break
    else:
        print("Opcion no valida")
           

   
        