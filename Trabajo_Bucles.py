# Bucles indeterminados (While).
# Se ejecutan un número indeterminado de veces.
# No se sabe a priori,cuántas veces se va a ejecutar el código de su interior.
# Se ejecutarán el número de veces que sean necesarias durante la ejecución del programa.

#Sintaxis.

#contador=0

#while contador<10:
    #print("Hola")
    #contador=contador+1
#print("Hemos salido del bucle")

#....................................................................


#edad=int(input("Introduzca su edad: "))

#while edad<0 or edad>100:
    #print("Edad no válida.")
    #edad=int(input("Introduzca su edad: "))


#print("Gracias, puede usted pasar")
#print("Edad del usuario: "+str(edad))

#........................................................................


# Instrucción (Break): Sale del bucle.

import math

print("Programa para hallar la raíz cuadrada de un valor numérico")

numero=int(input("Introduzca un número: "))

intentos=1

while numero<0:
    print("El número introducido no es válido.")

    numero=int(input("Introduzca un número válido: "))

    intentos=intentos+1

    if intentos==5:
        break


#Módulos (MATH)

if intentos==5:
    print("Número de intentos sobrepasado.")

else:
    print(math.isqrt(numero))



# Bucle (for) Determinado.


for i in [25,60,90]:
    print("Hola a todos")













