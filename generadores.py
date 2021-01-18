# Función tradicional.
"""
def numeros_pares(limite):
    num=1
    num_par=[]

    while num<limite:

        num_par.append(num*2)

        num+=1

    return num_par

print(numeros_pares(6))
"""


# Generador.

def numeros_pares(limite):
    num = 1

    while num < limite:
        yield num * 2

        num += 1


suc_pares = numeros_pares(6)  # El generador (numeros_pares), nos devuelve un objeto iterable, y lo almacena en una variable, (suc_pares), en este caso.

print(next(suc_pares))

print("Ahora va el siguiente valor: ")

print(next(suc_pares))

# (Yield from)

# Con bucles for anidados:

# def capitales_mundo(*ciudades): # El asterisco significa que el generador recibirá un número indeterminado de parámetros, y lo almacenará en forma de tupla.
# for capital in ciudades:
# for letra_capital in capital:
# yield letra_capital

# capitales_devueltas=capitales_mundo("Berlin", "Roma", "Bogotá", "Pekin", "Hanoi")

# print(next(capitales_devueltas))
# print(next(capitales_devueltas))
# print(next(capitales_devueltas))

# Con la instrucción yield for:

# def capitales_mundo(*ciudades): # El asterisco significa que el generador recibirá un número indeterminado de parámetros, y lo almacenará en forma de tupla.
# for capital in ciudades:

# yield from capital

# capitales_devueltas=capitales_mundo("Berlin", "Roma", "Bogotá", "Pekin", "Hanoi")

# print(next(capitales_devueltas))
# print(next(capitales_devueltas))
# print(next(capitales_devueltas))

# Repasar videos de generadores.
