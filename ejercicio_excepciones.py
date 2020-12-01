#Ejercicio excepciones. Agregar elemento en una lista

#Crea un programa que pida introducir por consola 10 nombres propios de personas.
#Los nombres se guardarán en una lista.
#Si introducimos un nombre repetido, el programa lanzará una excepción de tipo
#ValueError, la excepción nos informará del error con el texto “Error. Este nombre ya se
#ha introducido”, y no se guardará el nombre repetido en la lista.
#Imprimir el contenido de la lista por consola.


habituales=[]
c=1
while c<=10:
    try:
        nombres=(input("Introduzca un nuevo nombre: "))
        
        
        if nombres in habituales:
            raise ValueError

        else:
            habituales.append(nombres)
            c+=1

    except ValueError:
        print("El nombre", nombres, "ya se encuentra en la lista.")

print("los valores introducidos en la lista de habituales son: ", habituales)
