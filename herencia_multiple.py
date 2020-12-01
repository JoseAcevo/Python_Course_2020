class Persona:                                                                                                    # Clase padre (Superclase).
    
    def __init__(self, nombre, apellido, edad):                                                                     # Método constructor de la clase persona.
     
        self.nombre=nombre                                                                                          #
        self.apellido=apellido                                                                                      # Variable/ campo de clase.
        self.edad=edad                                                                                              #
        

    def getdatosPersonales(self):                                                                                   # Método/comportamiento de la clase creada.
        return "Nombre: " + self.nombre + " Apellido: " + self.apellido + " edad: " + str(self.edad) + " años"      # Devolución (return), de los datos personales a través del método (getdatospersonales (getter)).
                                                                                           
    def habla(self):                                                                                                #                         
        return "Estoy hablando"                                                                                     #
        
    def piensa(self):                                                                                               #
        return "Estoy pensando"                                                                                     # Mëtodos/ Comportamientos de la clase a la que pertenecen (clase padre o superclase, en este caso).

    def camina(self):                                                                                               #
        return "Estoy caminando"                                                                                    #

    def come(self):                                                                                                 #
        return "Estoy comiendo"                                                                                     #            

class Estudiante(Persona):                                                                                          # Nueva clase/ subclase (Hereda todos los métodos de la clase padre/ superclase (Persona)).

    def __init__(self, nombre, apellido, edad, escuela):                                                            # Método constructor de la subclase, la cual sobreescribe, el constructor heredado de la clase padre/superclase (Persona).
        Persona.__init__(self, nombre, apellido, edad)                                                              # Llamada al constructor de la clase padre/superclase (Persona).
        self.escuela=escuela

    def getdatosPersonales(self):
        return super().getdatosPersonales() + " Escuela: " + self.escuela

    def estudia(self):
        return "Estoy estudiando"


class Trabajador (Persona):

    def __init__(self, nombre, apellido, edad, empresa):
        Persona.__init__(self, nombre, apellido, edad)
        self.empresa=empresa

    def getdatosPersonales(self):
        return super().getdatosPersonales() + " Empresa: "  + self.empresa

    def trabaja(self):
        return "Estoy trabajando"
        
class Director (Estudiante, Trabajador):                                                                            # Creación de una nueva subclase la cual hereda, por órden de prioridad (izquierda a derecha), de las dos clases (Estudiante y trabajador).
    def __init__(self, nombre, apellido, edad, empresa, escuela, bonus):                                            # Creación de un constructor el cual sobreescribirá el método constructor heredado de la clase padre (Estudiante).

        Trabajador.__init__(self, nombre, apellido, edad, empresa)                                                  # Llamada al constructor de la clase (Trabajador).
        Estudiante.__init__(self, nombre, apellido, edad, escuela)                                                  # Llamada al constructor de la clase (Estudiante).
        self.bonus=bonus                                                                                            # Variable/campo de clase.
    
    def getdatosPersonales(self):
        return super().getdatosPersonales() + " Bonus: " + str(self.bonus) + " €"

    def dirige(self):
        return "Estoy dirigiendo"
    



persona=Persona("Jose", "García", 32)

estudiante=Estudiante("Pedro", "Fernández", 43, "San Javier")

print(persona.getdatosPersonales())
print(estudiante.getdatosPersonales())
print("--------------------------------------------------------------------------------------------")

trabajador1=Trabajador("Jose", "Pérez", 55, "Hermanos-Brunete s.l")
print(trabajador1.getdatosPersonales())

director1=Director("Jesus", "Murillo", 42, "HermanosBrunete", "San Juan", 1400)
print(director1.getdatosPersonales())


