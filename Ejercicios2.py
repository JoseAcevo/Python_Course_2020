"""

#def compara_listas (l1, l2):                               #Creación de una función a la que le pasamos dos listas por parámetros.

    
    #if (len(l1)!=len(l2)):                                 # Condicional (if) para comprobar si la longitud total de ambas listas es la misma.
        
        #return False                                       # En caso de no ser la misma longitud nos devuelve (False) y se saldría inmediatamente de la función.

    #else:                                                  # En caso de tener la misma longitud entrará en el bucle (For)..

        #for i in range(1,len(l1)):                         # Recorrido de todos los componentes de las listas, desde el elemento 1 y en toda su longitud (len).


            #if (l1[i])!=l2[i]:                             # Si elemento 1 de lista 1, diferente a elemento 1 de lista 2 devuelve (False), y se sale inmediatamente de la función.

                #return False

    #return True                                            # Si todos los elementos son iguales, nos devolverá (True,)


#A1=["Juan", "Jose", "Maria"]# Lista 1 (l1)

#A2=["Juan", "Jose", "Maria"]# Lista 2  (l2)


#print(compara_listas(A1, A2))                              # Función print con llamada a la función (compara_listas), pasándole a su vez ambas listas para su comprobación.



# IMPORTANTE REPASAR HASTA ENTENDERLO AL 100%

#Ejercicio 1:

paises={}                                                                                           # Creación de una variable países=(Diccionario)

pais=input("Introduzca un país, por favor: ")                                                       # Petición de entrada por teclado de un dato concreto, el cual queda almacenado en la variable (País).

while pais!="salir":                                                                                # Bucle While (Mientras),el dato previamente almacenado en la variable (País) sea DIFERENTE A (salir):
    ciudad=input("Introduzca una ciudad, por favor: ")                                              # Petición de un dato por teclado (una ciudad) para su almacenamiento en la variable(ciudad).
                                                                                                     
                                                                                                    # Si la encuentra (clave:país), devolverá su valor correspondiente.
    lista_ciudades=paises.setdef ault(pais,[ciudad])                                                 # Pregunta al método (.setdefault), por  la clave (país), en el diccinario (paises{})
                                                                                                    # En caso contrario, la creará, la almacenará en la variable (lista_ciudades) en forma de lista ([ciudad])
                                                                                                    # Y crea en el diccionario (países{}) la primnera pareja {clave:valor, España:Madrid} en su primera ejecución.                                                                                                 

    if lista_ciudades!=[ciudad]:                                                                    # Si (lista_ciudades) es diferente al dato/datos almacenados en la lista [ciudad]:  
        paises[pais].append(ciudad)                                                                 # Agrega al diccionario países{} en la clave [país], un nuevo valor (ciudad).

    pais=input("Introduzca un país, por favor: ")                                                   # En el caso de que (lista_ciudades),sea igual al dato/datos almacenados en la lista [ciudad]
                                                                                                     # Se hará una nueva petición por teclado de un nuevo dato y se almacenará en la variable (pais).
 
print(paises)                                                                                       # Impresión del diccionario (países{})

"""


# Ejercicios herencia. (POO)

class Vehiculo:
    def __init__(self, marca, modelo, color, ruedas, marchas):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.ruedas = ruedas
        self.marchas = marchas
        self.acelera = False
        self.frena = False
        self.arranque = False

    def datos_Veh(self):
        return "Datos del vehículo: " + "\nMarca: " + self.marca + "\nModelo: " + self.modelo + "\nColor: " + self.color + "\nNúmero de ruedas: " + str(
            self.ruedas)

    def arrancar(self):
        self.arranque = True
        if self.arranque:
            return "Hemos arrancado"

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True


class Coche(Vehiculo):

    def __init__(self, marca, modelo, color, ancho, alto, ruedas, marchas, n_plazas, aire, derrapar):
        Vehiculo.__init__(self, marca, modelo, color, ruedas, marchas)
        self.n_marchas = marchas
        self.n_plazas = n_plazas
        self.alto = alto
        self.ancho = ancho
        self.aire = aire
        self.derrapar = derrapar

    def datos_Veh(self):
        return super().datos_Veh() + "\nAncho del vehículo: " + str(
            self.ancho) + " mm." + "\nAlto del vehículo: " + str(self.alto) + " mm." + \
               "\nEl vehículo tiene: " + str(self.n_marchas) + " Velocidades" + " Y " + \
               str(self.n_plazas) + " plazas."

    def aire_Ac(self):

        if self.aire:
            return "El vehículo tiene aire acondicionado"

        else:
            return "El vehículo no tiene aire acondicionado"

    def derrape(self):

        if self.derrapar:
            return "Vamos de lado y sin manos......"

        else:
            return "Acelera coño...."

    def ir_Marcha_atras(self):

        return "Vamos marcha atrás."


class Furgoneta(Coche):

    def __init__(self, marca, modelo, color, ancho, alto, ruedas, marchas, n_plazas, aire, derrapar, carga):
        Coche.__init__(self, marca, modelo, color, ancho, alto, ruedas, marchas, n_plazas, aire, derrapar)
        self.carga = carga

    def cargando(self):

        if self.carga:
            return "\nLa furgoneta está cargada."
        else:
            return "\nLa furgoneta no está cargada."


class Bicicleta:
    def __init__(self, marca, modelo, color, ruedas, marchas, caballito):
        self.caballito = caballito

    def h_caballito(self):

        if self.caballito:
            return "Voy haciendo un caballito"

        else:
            return "Las dos ruedas en el suelo"


class Moto(Vehiculo, Bicicleta):
    def __init__(self, marca, modelo, color, ruedas, marchas, caballito, q_rueda):
        Vehiculo.__init__(self, marca, modelo, color, ruedas, marchas)
        Bicicleta.__init__(self, marca, modelo, color, ruedas, marchas, caballito)
        self.q_rueda = q_rueda

    def __str__(self):

        if self.q_rueda:
            return super().datos_Veh + "\nY estoy quemando una como si me las regalasen."
        else:
            return super().datos_Veh + "\nY no las estoy quemando, porque las ruedas son caras."


# V1 = Coche("Opel", "Vectra", "Rojo", 2500, 1500, 4, 5, 5, False, False, )
# print(V1.datos_Veh())
# print(V1.arrancar())
# print(V1.aire_Ac())
# print(V1.ir_Marcha_atras())
# V2=Furgoneta("Mercedes", "Viano", "Blanco",2350,1890,4,6,7,True, False,True)
# print(V2.datos_Veh())
# print(V2.Cargando())
# print(V2.aire_Ac())
# V3 = Moto ("Suzuki", "Katana", "Azul/blanca", 2, 1, False, False)
# print(V3.datos_Veh())
# V4 = Bicicleta("Orbea", "GR6000", "Roja", 2, 18, False)
# print(V4.h_caballito())
