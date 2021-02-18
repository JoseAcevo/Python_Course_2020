from io import open

modo = input("Introduzca el modo de apertura, (W) para modo escritura, (R) para modo lectura o (A) para modo adicción: ")
Modo = modo.lower()

if Modo == "w":
    archivo_externo = open("Primerarchivo.txt", "w")
    texto_1 = input("Introduzca el texto a guardar, por favor: ")
    archivo_externo.write(texto_1)
    archivo_externo.close()

elif Modo == "a":
    archivo_externo = open("Primerarchivo.txt", "a")
    texto_2 = input("Introduzca el texto a añadir, por favor: ")
    archivo_externo.write(texto_2)
    archivo_externo.close()

elif Modo == "r":
    archivo_externo = open("Primerarchivo.txt", "r")
    infoexterna = archivo_externo.readlines()
    archivo_externo.close()
    print("El archivo externo ha sido cargado.")
    busqueda = input("Introduzca el término a buscar, por favor: ")
    print(" ")

    for clave in infoexterna:
        if busqueda in clave:
            indice = clave.index(busqueda)

            print(
                f"En esta vuelta de bucle se ha/n encontrado el/los término/s seleccionado/s en "
                f"la siguente ubicación: \n{str.capitalize(clave[:])}\nCon el índice: {str([indice])}")
            print(" ")


        else:
            print("En esta vuelta de bucle no se ha/han encontrado el/los término/s seleccionado/s.")
            print(" ")

else:
    print("Petición no válida")

print("<<<<<<<<<<-----------Fin del programa---------------->>>>>>>>>>>>>")
