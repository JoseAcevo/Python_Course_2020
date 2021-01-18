# def sum(*args):
# value=0
# for n in args:
# value +=n
# return value
# print(sum(5,5,4,7,2,4,6))

# a="Jose"
# b="Acevo"
# x="%s %s" % (a,b)
# print(x)


# .Format
# Nombre=input("Introduce tu nombre: \n")
# Edad=int(input("Introduce tu edad: \n"))
# Nombre_mascota=input("Introduce el nombre de tú mascota: \n")
# print("Tú nombre es ", Nombre, "Tienes", Edad, "años", "Tú mascota se llama ", Nombre_mascota)
# print("Tú nombre es {0} tienes {1} años y tú mascota se llama {2}".format(Nombre, Edad, Nombre_mascota))

# for x in range (1,11):
# print("{3}{0:2d}{3} {3}{1:3d}{3} {3}{2:4d}{3}".format(x,x*x,x*x*x,"|"))

# a = "abra"
# b = "cad"
# print("{0:<9} {1:^9} {0:>9}".format(a, b))


def capital_cities(**kwargs):
    # initialize an empty list to store the result
    result = []
    for key, value in kwargs.items():
        result.append(f'The capital of {key} is {value}')
    return result


print(capital_cities(China='Beijing', Cairo='Egipt', Rome='Italy'))


