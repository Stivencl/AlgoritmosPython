def suma(a, b):
    return a+b

def resta(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    if b !=0:
        return a/b
    else:
        return "Error:division por cero"

def mostrar_menu():
    print("calculadora basica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
while True:
    mostrar_menu()
    opcion = input("Elige una opción")
    
    if opcion == "5":
        print("Gracias por usar la caluladora")
        break
    
    if opcion in ["1", "2", "3", "4"]:
            num1 = float(input("Digite primer número..."))
            num2 = float(input("Digite segundo número..."))
    
            if opcion == "1":
                print(f"Resultado: {suma(num1, num2)}")
            elif opcion == "2":
                print(f"Resultado: {resta(num1, num2)}")
            elif opcion == "3":
                print(f"Resultado: {multi(num1, num2)}")
            elif opcion == "4":
                print(f"Resultado: {div(num1, num2)}")
    else:
        print("Opcion no valida")
    
    
    