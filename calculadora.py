def main():
    ans = 0
    print("Bienvenido a la calculadora de Lince")
    print("Por favor, ingrese dos números")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print("Por favor, ingrese la operación que desea realizar")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Módulo")
    operacion = int(input("Ingrese el número de la operación: "))
    if operacion == 1:
        # ans = suma(num1, num2)
        print(f"El resultado de la suma es: {ans}")
    elif operacion == 2:
        # ans = resta(num1, num2)
        print(f"El resultado de la resta es: {ans}")
    elif operacion == 3:
        # ans = multiplicacion(num1, num2)
        print(f"El resultado de la multiplicación es: {ans}")
    elif operacion == 4:
        # ans = division(num1, num2)
        print(f"El resultado de la división es: {ans}")
    elif operacion == 5:
        # ans = modulo(num1, num2)
        print(f"El resultado del módulo es: {ans}")
    else:
        print("Operación no válida")

main()