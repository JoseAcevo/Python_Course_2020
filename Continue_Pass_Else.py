# Continue:

#Contador de caracteres.

# Con función (len).

#nombre="Jose Manuel"

#print(len(nombre))# El problema es que contabiliza el espacio en blanco, como un caracter más.

# Con función (Continue).

#nombre="Jose Manuel"

#contador=0  # Variable (contador) cuenta el número de caracteres.

#for i in nombre:
    #contador+=1

#print(contador)

#Continua contabilizando el espacio en blanco como un caracter más.

nombre="Jose Manuel"


contador=0

for i in nombre:

    if i==" ":
        continue

    contador+=1

print(contador)

# No se tiene en cuenta el espacio en blanco en el cómputo final del número de caracteres.

# Función (Pass).

# Se utiliza para posponer un determinado trabajo y no nos de fallo al ejecutar el programa.

# Función (else), fuera de los condicionales y dentro de un bucle.

email=input("Introduzca su dirección de correo: ")

for i in email:

    if i=="@":

        arroba=True

        break

else:
    arroba=False

print(arroba)

# Si i es igual a @ en algún punto al recorrer la dirección suministrada, entrará en el if y a continuación "romperá", lo que nos devolverá, True.
# Si i no es igual a @ en ningún punto al recorrer la dirección suministrada, el bucle continuará buscando hasta que termine de recorrer la dirección, y a continuación, entrará en el else.
#devolviéndonos (False).









































