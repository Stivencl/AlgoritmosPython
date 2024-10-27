class GertionTareas:
    def __init__(self, titulo, detalle, estado):
        self.titulo = titulo
        self.detalle = detalle
        self.estado = estado
        
def mostrar_menu():
    print("Gestión de tareas")
    print("1. Agregar tarea")
    print("2. Mostrar tarea")
    print("3. Buscar tarea")
    print("4. Actualizar estado")
    print("5. eliminar tarea")
    print("6. Filtrar tares por estado NC: No Completas, C: Completas")
    print("7. Salir")
            
tareas = []

while True:
    mostrar_menu()
    opc = input("Elige la opcion deseada\n")
    
    if opc == "7":
        print("Gracias por utilizar el gestor de treas 1.0")
        break
    
    if opc == "1":
        try:
            titulo =  str(input("Escriba el nombre de la tarea\n")).upper()
            detalle = str(input("Escriba el detalle de la tarea\n")).upper()
            estado = str(input("Escriba el estado de la tarea NC: no completa, C: completa\n")).upper()
            if estado == "NC" or estado == "C":
              tarea = GertionTareas(titulo, detalle, estado)
              tareas.append(tarea)
              print("Tarea agregda con exito\n")
            else:
                raise NameError("Error")    
        except NameError:
            print("Errro: Esatdo de la tarea")
            
    elif opc == "2":
         for i in tareas:
             print(f"Titulo: {i.titulo}, Detalle: {i.detalle}, Estado: {i.estado}")
             
    elif opc == "3":
            
                titulo = str(input("Escriba el titulo de la tarea")).upper()
                
                for i in tareas:
                     if i.titulo == titulo:
                         print(f"Titulo:{i.titulo}, Detalle: {i.detalle}, Estado: {i.estado}")
                        
                         break                                                         
    elif opc == "4":
        
        titulo = input("Escribe el nombre de la tarea\n")
        try:
           estadoNuevo = str(input("Actaliza el estado de la tarea NC: no completa, C: completa\n")).upper()
           if estadoNuevo == "NC" or estadoNuevo == "C":
                    for i in tareas:
                        if titulo == i.titulo:
                            i.estado = estadoNuevo
                            print("Estado actulizado")
                            break
           else:
                raise NameError()         
        except NameError:
            print("Error: Valores no encontrados") 
    elif opc == "5":
        try:
           titulo = input("Escribe el nombre de la tarea a eliminar\n").upper()
           for i in tareas:
               if i.titulo == titulo:
                   tareas.remove(i)
                   print("Tarea eliminada") 
                   break
               else:
                   raise NameError()
        except NameError:
            print("Error: tarea no encontrada")
    elif opc ==  "6":
        try:
            estado = str(input("Filtrar tarea por estdo, Digite NC o C\n")).upper()
            for i in tareas:
                if i.estado == estado:
                     print(f"Titulo: {i.titulo}, Detalle: {i.detalle}, Estado: {i.estado}")
                elif i.estado == estado:
                 print(f"Titulo: {i.titulo}, Detalle: {i.detalle}, Estado: {i.estado}")
            else:
                raise NameError()     
        except NameError:
            print("Error: Valores invalidos")        
                            
    else:
        print("Opcion no valida, intente nuevamente")                                
        
                       