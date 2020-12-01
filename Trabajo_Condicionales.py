#Nota_alumno=int(input("Introduzca su nota: "))# Petición de un dato por consola, se utiliza la función predefinida (Int), porque vamos a solicitar la introducción de un parámetro de tipo (entero).

#def evaluacion_alumno(nota):# Creación de la función, con paso de parámetros/argumentos, en este caso (nota)

    #valoracion="Desconocida"# Creación de la variable (Valoración) cuyo parámetro es (Desconocida)

    #if nota < 5:
        #valoracion="Suspenso"# Si valoración < 5 = (Suspenso).

    #elif nota > 10:
        #valoracion="Nota errónea"# Si valoración > 10 = (Nota errónea).

    #else:
        #valoracion="Aprobado"# Si valoración ninguna de las anteriores = Aprobado
    
    #return valoracion # Devolución del dato almacenado en (Valoración).

#print(evaluacion_alumno(Nota_alumno))# Impresión en consola..¿..........?.

#..................................................................................................................................................................................

#Uso del condicional (Elif).

# print("Programa de evaluación de alumnos 2020")

# Nota_alumno=int(input("Introduzca su nota, por favor: "))

# if Nota_alumno < 5:
    #print("Insuficiente")

# elif Nota_alumno < 6:
    #print("Suficiente")

# elif Nota_alumno < 7:
    #print("Bien")

# elif Nota_alumno < 9:
    #print("Notable")

# else:
    #print ("Sobresaliente")

#.............................................................................................................

# Uso de los operadores lógicos (and y or):

# Sin operadores lógicos.
# print ("Programa para la obtención del carnet de conducir")

# edad=int(input("Introduzca su edad, por favor: "))


# if 18<edad<90:
    #print("Los requisitos se cumplen, puede optar a la obtención.")

# else:
    #print("Los requisitos no se cumplen, no puede obtar a la obtención.")


# Con el operador lógico (And).

# A

#print("Programa para la obtención del carnet de conducir")

#edad=int(input("Introduzca su edad, por favor: "))


#if edad >= 18 and edad <= 90:
    #print("Los requisitos se cumplen, puede optar a la obtención.")

#else:
    #print("Los requisitos no se cumplen, no puede obtar a la obtención.")

# B

#print ("Programa para la obtención del carnet de conducir")

#edad=int(input("Introduzca su edad, por favor: "))

#opcion=input("Tiene su visión en un estado aceptable, (Si/No): ")

#vision=opcion.lower()

#if edad >= 18 and edad <=90 and vision =="si":
    #print("Los requisitos se cumplen, puede optar a la obtención")

#else:
    #print("Los requisitos no se cumplen, no puede obtar a la obtención.")

# Con el operador lógico (or)

#print("Programa de control de concesión de becas de estudios 2020")

#nota_media=int(input("Introduzca su nota media: "))

#hermanos_centro=int(input("Introduzca el número de hermanos: "))

#distancia_centro=int(input("Introduzca la distancia en km, hasta el centro de estudios: "))

#renta_familiar=int(input("Introduzca renta familiar: "))

#if nota_media > 8 and hermanos_centro > 3 and distancia_centro > 10 or renta_familiar < 20000:
    #print("La beca será concedida")

#else:
    #print("No tiene derecho a beca")

# Con el operador lógico (or), y con el uso de paréntesis..(). Es muy importante como ordenar los datos entre los paréntesis, ya que influirá en el resultado dado por el programa.


#print("Programa de control de concesión de becas de estudios 2020") # Impresión en consola del título del programa.

#nota_media=int(input("Introduzca su nota media: "))# Petición por consola del dato (Nota_media)

#hermanos_centro=int(input("Introduzca el número de hermanos: "))# Petición por consola del dato (Número_hermanos)

#distancia_centro=int(input("Introduzca la distancia en km, hasta el centro de estudios: "))# Petición por consola del dato ( Distancia_centro_estudios)

#renta_familiar=int(input("Introduzca renta familiar: ")) # Petición por consola del dato ( Renta_familiar)

#if (nota_media > 8 and hermanos_centro > 3 and distancia_centro > 10) or renta_familiar < 20000:  # Mucho cuidado con los paréntesis, pueden cambiar el resultado de un programa.
# Condicional (if), con los operadores lógicos (and y or), (y con el uso de paréntesis, para la validación de los resultados almacenados en las variables).
    #print("La beca será concedida")# Impresión en consola del resultado final.

#else:
    #print("No tiene derecho a beca")# Impresión en consola del resultado final, en el caso de no cumplirse el (if)

#........................................................................................................................................


# Operadores (Not e In).
# Utilizados en una lista:

# lista_trabajadores=["Jose", "Paula","Manuel", "Ana", "Sandra"]

#if "Jose" in lista_trabajadores:
    #print("Está en la lista")

#else:
    #print("No está en la lista")

# Utilizados en un string:

#lenguajes_trim1="Java", "Php", "Python", "C#", "Html", "JavaScript"

#if "Java" in lenguajes_trim1:
    #print("Está presente")

#else:
    #print("No está presente")

# (Not) utilizado en una lista.

#if "Jose" not in lista_trabajadores:
    #print("No está en la lista")

#else:
    #print("Está en la lista")

#if not "Jose" in lista_trabajadores:
    #print("No está en la lista")

#else:
    #print("Está en la lista")
#..........................................................................



