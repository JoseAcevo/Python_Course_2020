#Instrucción (Continue):

#Contabilizar número de caracteres función (len). Se contabilizan también los espacios en blanco como caracteres.

nombre="Jose Manuel"
print(len(nombre))


#Contabilizar número de caracteres (con un bucle (for)). Se contabilizan también los espacios en blanco como caracteres.

nombre="Jose Manuel"

contador=0

for i in nombre:
    contador+=1

print(contador)

#Contabilizar número de caracteres (con un bucle (for + condicional if + función (continue)).  No se contabilizarán los espacios en blanco como caracteres.


nombre="Jose Manuel"

contador=0

for i in nombre:

    if i==" ":
        continue

    contador+=1

print(contador)


# Instrucción (pass).
# Su uso es temporal, se utiliza para que el programa no de error en su ejecución al encontrarse con código sin completar.

#Instrucción (else).

email=input("Introduzca su dirección de email: ")

for i in email:

    if i == "@":

        arroba=True

        break

else:

    arroba=False
 
print(arroba)