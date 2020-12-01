def suma(n1, n2):
    return n1 + n2


def resta(n1, n2):
    return n1 - n2


def multiplicacion(n1, n2):
    return n1 * n2


def division(n1, n2):
    try:
        return n1 / n2

    except ZeroDivisionError:
        print("No se puede dividir entre 0.")
        return "Operación no soportada."


Variable_Contador = 1

while Variable_Contador <= 3:

    try:

        operando1 = int(input("Introduzca el primer valor, por favor: "))
        operando2 = int(input("Introduzca el segundo valor, por favor: "))

        operacion = input("¿Que operación quiere realizar (suma, resta, multiplicación o división: ")
        operacion = operacion.lower()

        if operacion == "suma":
            print(suma(operando1, operando2))
            break


        elif operacion == "resta":
            print(resta(operando1, operando2))
            break

        elif operacion == "multiplicacion":
            print(multiplicacion(operando1, operando2))
            break

        elif operacion == "division":
            print(division(operando1, operando2))
            break


        else:
            print("Operación errónea.")
            break

    except ValueError:
        print("Valor introducido incorrecto.")
        Variable_Contador += 1
        if Variable_Contador == 4:
            print("Has consumido demasiados intentos.", end=" ")

print("El programa ha finalizado.")
