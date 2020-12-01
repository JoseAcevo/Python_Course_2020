class Persona:                                                                                           # Clase padre (superclase)

    def __init__(self, nombre, apellido, edad):                                                          # Método constructor de la clase persona.

        self.nombre = nombre                                                                             #
        self.apellido = apellido                                                                         # Variable/ campo de clase.
        self.edad = edad                                                                                 #

    def getdatosPersonales(self):                                                                        # Método/comportamiento de la clase creada.
        return "Nombre: " + self.nombre + " Apellido: " + self.apellido + " edad: "\
             + str+(self.edad) + " años"                                                                 # Devolución (return), de los datos personales a través del método (getdatospersonales (getter)).

    def habla(self):                                                                                     #
        return "Estoy hablando"                                                                          #

    def piensa(self):                                                                                    #
        return "Estoy pensando"                                                                          # Mëtodos/ Comportamientos de la clase a la que pertenecen (clase padre o superclase, en este caso).

    def camina(self):                                                                                    #
        return "Estoy caminando"                                                                         #

    def come(self):                                                                                      #
        return "Estoy comiendo"                                                                          #


class Estudiante(Persona):                                                                               # Nueva clase/ subclase (Hereda todos los métodos de la clase padre/ superclase (Persona)).

    def __init__(self, nombre, apellido, edad, escuela):                                                 # Método constructor de la subclase, el cual sobreescribe el constructor heredado de la clase padre/superclase (Persona).
        Persona.__init__(self, nombre, apellido, edad)                                                   # Llamada al constructor de la clase padre/superclase (Persona).
        self.escuela = escuela                                                                           # Creación de un nuevo campo/variable de clase propia de la subclase. (NO HEREDADA)

    def getdatosPersonales(self):                                                                        # Creacion del método getdatosPersonales de la subclase (Persona).
        return super().getdatosPersonales() + " Escuela: " + self.escuela                                # Llamada al método getdatosPersonales de la clase padre/superclase, a la cual se añadirá la variable de la subclase (Estudiante).

    def estudia(self):                                                                                   # Cración de un nuevo método (estudia) de la subclase (Estudiante).
        return "Estoy estudiando"                                                                        # Devolución del mensaje "Estoy estudiando".


class Trabajador(Persona):                                                                               # Creación de una nueva subclase (Trabajador), heredando de la clase padre/superclase (Persona).

    def __init__(self, nombre, apellido, edad, empresa):                                                 # Creación del método constructor de la subclase, el cual, sobreescribe el método constructor heredado de la superclase/ clase padre (Persona) para de esta manera poder asignar un nuevo dato/ parámetro (empresa).
        Persona.__init__(self, nombre, apellido, edad)
                                                                                                         # Llamada al método constructor de la clase padre/ superclase (Persona).
        self.empresa = empresa                                                                           # Creación de una nueva variable/ campo de clase de la subclase correspondiente (Trabajador).

    def getdatosPersonales(self):                                                                        #Creación de un nuevo método (getdatosPersonales) de la subclase (Trabajador).
        return super().getdatosPersonales() + " Empresa: " + self.empresa                                # Llamada al método getdatosPersonales de la clase padre/superclase, para de esta manera, poder añadir la información de la nueva variable/campo de clase de la subclase correspondiente (Trabajador).

    def trabaja(self):                                                                                   # Creación de un nuevo método de la subclase (Trabajador)
        return "Estoy trabajando"                                                                        # Devolución del mensaje "Estoy trabajando".


class Director(Estudiante, Trabajador):                                                                  # Creación de una nueva subclase la cual hereda, por órden de prioridad (izquierda a derecha), de las dos clases (Estudiante y trabajador) (HERENCIA MÚLTIPLE)
    def __init__(self, nombre, apellido, edad, empresa, escuela, bonus):                                 # Creación de un constructor el cual sobreescribirá el método constructor heredado de la clase padre (Estudiante).

        Trabajador.__init__(self, nombre, apellido, edad, empresa)                                       # Llamada al constructor de la clase (Trabajador).
        Estudiante.__init__(self, nombre, apellido, edad, escuela)                                       # Llamada al constructor de la clase (Estudiante).
        self.bonus = bonus                                                                               # Variable/campo de clase.

    def getdatosPersonales(self):                                                                        # Creación de un nuevo método (getdatosPersonales) de la subclase (Director).
        return super().getdatosPersonales() + " Bonus: " + str(
            self.bonus) + " €"                                                                           # Llamada al método (getdatosPersonales) de la clase padre/superclse, para poder añadir la información de la nueva variable/ campo de clase (bonus).

    def dirige(self):                                                                                    # Creación de un nuevo método propio de la subclase (Director).
        return "Estoy dirigiendo"                                                                        # Devolución del mensaje ("Estoy dirigiendo").


persona = Persona("Jose", "García", 32)                                                                  # Creación de un objeto/instancia de clase de tipo (Persona), con el paso de los parámetros exigidos por dicha clase.

estudiante = Estudiante("Pedro", "Fernández", 43, "San Javier")                                          # Creación de un objeto/instancia de clase de tipo (Estudiante), con el paso de los parámetros exigidos por dicha clase.

print(persona.getdatosPersonales())                                                                      # Impresión en consola de los datos (datos personales) del objeto (persona).
print(estudiante.getdatosPersonales())                                                                   # Impresión en consola de los datos (datos personales) del objeto (estudiante).
print("--------------------------------------------------------------------------------------------")

trabajador1 = Trabajador("Jose", "Pérez", 55, "Hermanos-Brunete s.l")                                    # Creación de un objeto/instancia de clase (trabajador1) de tipo (Trabajador), con el paso de los parámetros exigidos por dicha clase.
print(trabajador1.getdatosPersonales())                                                                  # Impresión en consola de los datos (datos personales) del objeto (trabajador1).

director1 = Director("Jesus", "Murillo", 42, "HermanosBrunete", "San Juan", 1400)                        # Creación de un objeto/instancia de clase (director1) de tipo (Director), con el paso de los parámetros exigidos por dicha clase.
print(director1.getdatosPersonales())                                                                    # Impresión en consola de los datos (datos personales) del objeto (Director1).
