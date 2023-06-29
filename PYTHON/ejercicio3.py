def realizar_operacion(numero1, numero2, operador):
    if operador == "+":
        resultado = numero1 + numero2
    elif operador == "-":
        resultado = numero1 - numero2
    elif operador == "*":
        resultado = numero1 * numero2
    elif operador == "/":
        resultado = numero1 / numero2
    else:
        print("Operador inválido.")
        return None
    return resultado

# Solicitar entrada al usuario
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
operador = input("Ingrese el operador (+, -, *, /): ")

# Realizar la operación y mostrar el resultado
resultado = realizar_operacion(numero1, numero2, operador)
if resultado is not None:
    print("El resultado es:", resultado)