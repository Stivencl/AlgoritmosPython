class Contacto:
    def __init__(self, nombre, telefono):
        
        self.nombre = nombre
        self.telefono = telefono
    
def mostrar_menu():
    print("Gestion de contactos")
    print("1, Agregar contacto")
    print("2. Mostrar contacto")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
        
contactos=[]
        
while True:
    mostrar_menu()
    opcion = input("Elige una opcion")
        
    if opcion == "5":
        print("Saliendo del programa")
        break
    if opcion == "1":
        nombre = input("Ingrese el nombre")
        telefono = input("Ingrese el telefono")
        contacto = Contacto(nombre, telefono)
        contactos.append(contacto)
    elif opcion == "2":
        for c in contactos:
            print(f"Nombre: {c.nombre}, telefono: {c.telefono}")
    elif opcion == "3":
        nombre = input("Ingrese el nombre a buscar")
        encontrado = False
        for c in contactos:
            if c.nombre == nombre:
                print(f"nombre: {c.nombre}, telefono: {c.telefono}")
                encontrado = True
                break
        if not encontrado:
            print("Contacto no encontrado")
    elif opcion == "4":
        nombre = input("Ingrese el nombre a eliminar")
        for c in contactos:
            if c.nombre == nombre:
                contactos.remove(c)
                print("COntacto eliminado")
                break
    else:
        print("Opcion no valida intente de nuevo")    
        
        