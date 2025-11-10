def suma (a,b):
    return a + b
def resta(a,b):
    return a - b
def multiplicar(a,b):
    return(a * b)
def division(a,b):
    return a / b

def menu():
    print("Bienvenido a la calculadora de base")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicar")
    print("4.División")
    print("5. Salir")

def main():
    while True:
        menu()
        try:
                opcion = int(input("Ingrese una opcion: "))

                num1 = int(input("Ingrese el primer numero:  "))
                num2 = int(input("Ingrese el segundo numero: "))

                match opcion:
                     
                    case 1:
                        resultado = suma(num1,num2)
                    
                    case 2:
                        resultado = resta(num1,num2)
                    
                    case 3:
                        resultado = multiplicar(num1,num2)
                    case 4: 
                        resultado = division(num1,num2)

                    case 5:
                        print("Saliendo")
                        break
                    case _:
                        print("La opcion ingresada no existe")
        except ValueError:
            print("El valor ingresado no es válido")
        except ZeroDivisionError:
            print("NO se puede dividir por 0")
        else:
            print(f"el resultado es: {resultado}")
