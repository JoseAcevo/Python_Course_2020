# Condicionales: (a)

# Ejercicio 1:
# Crea un programa que pida dos números por teclado. El programa tendrá una función-
# llamada “DevuelveMax” encargada de devolver el número más alto de los dos introducidos.

# N1=(int(input("Introduzca el primer número: ")))
# N2=(int(input("Introduzca el segundo número: ")))

# def devuelve_Max (N1, N2):
# if N1 < N2:
# print("segundo.")

# elif N2 < N1 :
# print("primero.")

# else:
# print("\nAmbos números son iguales.")

# print("El número más alto es el ", end="")

# devuelve_Max(N1, N2)

# ..........................................................................................................
# Condicionales: (b)

# N1=(int(input("Introduzca el primer número: "))) # Entrada por teclado del primer valor.
# N2=(int(input("Introduzca el segundo número: ")))# Entrada por teclado del segundo valor.

# def devuelve_valor (N1, N2):# Declaración de la función.
# if N1 < N2:
# print("El número más alto es el segundo.")
# elif N2 < N1:
# print("El número más alto es el primero.")
# else:
# print("Ambos números son iguales.")

# devuelve_valor(N1, N2)# Invocación de la función.

# ................................................................................................................

# Ejercicio 2:

# Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos.
# deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos.
# personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por.
# teclado).

# Nombre = (input("Introduzca su nombre: "))# Entrada por teclado del primer valor (Nombre).
# Dirección = (input("Introduzca su dirección: "))# Entrada por teclado del segundo valor (Dirección).
# Teléfono = (input("Introduzca su número de teléfono: "))# Entrada por teclado del tercer valor (Teléfono).

# lista_datos=[Nombre, Dirección, Teléfono]# Creación de la lista para el almacenaje de los datos previamente introducidos.

# print("Los datos introducidos son: " +

# "\nNombre: " + lista_datos[0] +

# "\nDirección: " + lista_datos[1] +

# "\nTeléfono: " + lista_datos[2]) # Impresión en consola del mensaje, como se pide en el ejercicio, pero insertando saltos de linea con el comando (\n).

# .................................................................................................................................................................

# Ejercicio 3:

# Crea un programa que pida cinco números por teclado. El programa imprime en consola la media aritmética de los números introducidos.

# N1 = (int(input("Introduzca el primer número: ")))
# N2 = (int(input("Introduzca el segundo número: ")))
# N3 = (int(input("Introduzca el tercer número: ")))
# N4 = (int(input("Introduzca el cuarto número: ")))
# N5 = (int(input("Introduzca el quinto número: ")))

# media=(N1+N2+N3+N4+N5)/5

# print("La media aritmética es: ",  end="")

# print(media)

# *Media aritmética:
# Se obtiene a partir de la suma de todos sus sumandos dividida entre el número de ellos. 

# ......................................................................................................................

# print("Programa de control de los tipos impositivos para la declaración de la renta 2020.")

# renta=float(input("Introduzca su nivel de renta, por favor: "))

# if renta <3.000:
# print("Este tipo de renta está exento de impuestos.")

# elif renta >= 3.000 and renta <= 12.000:
# print:("A la renta entre 3.000 y 12.000 le corresponde un 7% de tipo impositivo.")

# elif renta >=12.000 and  renta <=18.000:
# print("A la renta entre 12000 y 18000 le corresponde un 15% de tipo impositivo.")

# elif renta >=18.000 and renta <=35.000:
# print("A la renta entre 18.000 y 35.000 le corresponde un 21% de tipo impositivo.")

# elif renta >=35.000 and renta <=70.000:
# print("A la renta entre 35.000 y 70.000 le corresponde un 35% de tipo impositivo")

# else:
# print("A ese nivel de renta le corresponde un 45% de tipo impositivo")


# .......................................................................................................

# Ejercicio bucles y condicionales. Número aleatorio
# Se trata de elaborar un programa que genere un número aleatorio entre 1 y 100. Para ello
# debemos importar el módulo random y utilizar la instrucción random.randint(1,100). Esta
# instrucción genera un número entero entre 1 y 100.
# A continuación, se le pide al usuario que introduzca un número por consola entre 1 y 100. Si el
# número introducido por el usuario es menor, se imprime en consola un mensaje indicando que
# el número aleatorio es mayor que el introducido por él. Si el número introducido por el usuario
# es mayor que el aleatorio, se imprime un mensaje indicando que el número aleatorio es menor
# que el introducido por él. Después de indicar si es mayor o menor, se vuelve a pedir al usuario
# que introduzca un número entre 1 y 100.
# Se trata de averiguar cuál es el número aleatorio generado por el programa a base de ir
# aproximándonos intento tras intento, y hacerlo en el menor número de intentos posibles así que
# también debemos controlar cuántos intentos consume el usuario para adivinar el número
# aleatorio generado por el programa.
# Cuando el usuario averigüe finalmente el número aleatorio, el programa imprimirá en consola
# “Correcto. Has utilizado…” y el nº de intentos consumidos

import random

print("Come on man....Play with me...Do it in less than 10 attempts... If you can....:-) ")


def main():
    al_number = random.randint(1, 100)
    n_user = int(input("Enter a number between one and one hundred please: "))
    attempts = 1

    while al_number != n_user:
        try:
            if n_user < al_number:
                print("The entered number must be higher.")
                attempts += 1
                n_user = int(input("Enter a new number please: "))

            if n_user > al_number:
                print("The entered number must be lower.")
                attempts += 1
                n_user = int(input("Enter a new number please: "))

        except ValueError:
            print("WRONG VALUE")
            new_attempt()

    if n_user == al_number and attempts < 10:
        print(f"CONGRATS...You only has needed {str(attempts)} attempts.")
        new_attempt()

    elif n_user == al_number and attempts == 10:
        print("OOOOMMMMMMMGGGGGG...Just in time....")
        new_attempt()

    else:
        print(f"Correct, but you´ve needed {str(attempts)} attempts. Try it one more time !!!!")
        new_attempt()


def new_attempt():
    option = input("Do you want a new attempt (yes or not)?: ")
    l_option = option.lower()
    attempt = 1

    if l_option == "yes":
        print("<-----New game is ready----->")
        main()

    if l_option == "not":
        print("Thanks a lot for participate, see you next the time.....")

    while l_option != "yes" and l_option != "not":
        option = input("Please, insert a valid answer (yes or not): ")
        l_option = option.lower()
        attempt += 1

        if l_option == "yes":
            print("<-----New game is ready----->")
            main()

        if l_option == "not":
            print("Thanks a lot for participate, see you the next time.....")
            break

        if attempt == 5:
            print("Maximum number of attempts exceeded, thanks for participate...Byeee")
            print("<<<<<<<<<<<<<<<<<GAME OVER>>>>>>>>>>>>>>>>>>")
            break


if __name__ == '__main__':
    main()
