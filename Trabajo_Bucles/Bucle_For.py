# Bucle determinado FOR.
# Impresión de las claves de un diccionario, utilizando para ello un (bucle for).

capitales = {"China": "Pekin", "India": "Nueva Delhi", "Indonesia": "Yakarta", "Japón": "Tokio", "Bangladesh": "Dacca"}

for clave in capitales:
    print(clave)

# Impresión de la clave y su valor correspondiente.

capitales = {"China": "Pekin", "India": "Nueva Delhi", "Indonesia": "Yakarta", "Japón": "Tokio", "Bangladesh": "Dacca"}

for clave in capitales:
    valor = capitales[clave]
    print(clave)
    print(valor)

# Impresión de todos los elementos de un diccionario. ( .items() ).

capitales = {"China": "Pekin", "India": "Nueva Delhi", "Indonesia": "Yakarta", "Japón": "Tokio", "Bangladesh": "Dacca"}

for clave in capitales:
    valor = capitales[clave]
    print(clave)
    print(valor)

print(capitales.items())

# Recorrido de clave+valor en un dicionario, asociándolos con un símbolo, por ejemplo: (->).

capitales = {"China": "Pekin", "India": "Nueva Delhi", "Indonesia": "Yakarta", "Japón": "Tokio", "Bangladesh": "Dacca"}

for clave, valor in capitales.items():
    print(clave + "->" + valor)

# Código aparte, salido de un ejercicio. (No forma parte del curso de Juan)
number_list = []

for numbers in range(2, 21):
    number_list.append(numbers)


def delete_items():
    for elements in number_list:         # Aquí no se incrementa el valor de (i) en cada pasada de bucle, se evalúan los elementos dentro de la lista.
        # print(elements)                # Imprime el elemento que estás evaluando (En la primera vuelta de bucle, será el primer elemento).
        number_list.remove(elements)     # Eliminará ese primer elemento de la lista.
        # print(elements)                # Imprime de nuevo el elemento que está siendo evaluado, aunque ya haya sido eliminado.
    print(number_list)


delete_items()
