import math


def calcula_raiz_cuadrada(numero):
    if numero < 0:

        raise ValueError("El valor no puede ser negativo")

    else:

        return math.sqrt(numero)


Nusuario = (int(input("Introduzca un valor: ")))

try:

    print(calcula_raiz_cuadrada(Nusuario))

except ValueError:

    print("Introducción de valor erróneo.")

print("Y por aquí continuaría el programa")
