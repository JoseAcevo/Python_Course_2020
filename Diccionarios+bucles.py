# Impresión de las claves de un diccionario, utilizando para ello un (bucle for).

capitales = {"China": "Pekin", "India": "Nueva Delhi", "Indonesia": "Yakarta", "Japón": "Tokio", "Bangladesh": "Dacca"}

for clave in capitales:
    print(clave)

# Impresión de la clave y su valor correspondiente.

capitales = {"China": "Pekin", "India": "Nueva Delhi", "Indonesia": "Yakarta", "Japón": "Tokio", "Bangladesh": "Dacca"}

for clave in capitales:
    valor=capitales[clave]
    print(clave)
    print(valor)



# Impresión de todos los elementos de un diccionario. ( .items() ).

capitales = {"China":"Pekin", "India":"Nueva Delhi","Indonesia":"Yakarta","Japón":"Tokio","Bangladesh":"Dacca"}

for clave in capitales:
    valor=capitales[clave]
    print(clave)
    print(valor)

print(capitales.items())

# Recorrido de clave+valor en un dicionario, asociándolos con un símbolo, por ejemplo: (->).

capitales = {"China":"Pekin", "India":"Nueva Delhi","Indonesia":"Yakarta","Japón":"Tokio","Bangladesh":"Dacca"}

for clave, valor in capitales.items():
    print(clave + "->" + valor)
    