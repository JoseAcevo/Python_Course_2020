class Persona:                                                                                                                              # Clase padre (Superclase).
    def __init__(self, nombre, apellido, edad):                                                                                             # Método constructor de la clase el cual otorgará unas propiedades/estado inicial a todos los objetos/ instancias que pertenezcan a la clase.
        
        self.nombre=nombre                                                                                                                  #
        self.apellido=apellido                                                                                                              # Propiedades/ campos de clase.
        self.edad=edad                                                                                                                      #

    def getdatosPersonales(self):                                                                                                           # Método  de la clase padre.
        return "Nombre: " + self.nombre +" Apellido: " + self.apellido + " edad: " + str(self.edad)                                         # Comportamiento del método creado.
        
    def habla(self):                                                                                                                        # Mëtodo de la clase padre.
        return "Estoy hablando"                                                                                                             # Comportamiento del método creado.
        
    def piensa(self):
        return "Estoy pensando"

    def camina(self):
        return "Estoy caminando"

    def come(self):
        return "Estoy comiendo"

class Estudiante(Persona):                                                                                                                  # Creación de una nueva clase (subclase), ya que hereda de la case padre (superclase), Persona.

    def __init__(self, nombre, apellido, edad, escuela):                                                                                    # Sobreescritura/ invalidación del método constructor heredado de la clase padre (Persona), para crear el constructor de la clase (estudiante).
        super().__init__(nombre, apellido, edad)                                                                                            # Llamada al método constructor de la clase padre, para no tener que repetir el código de su interior, y que el constructor de la subclase sepa que hacer con las variables/campos de clase (nombre, apellido, edad).
        self.escuela = escuela                                                                                                                # Propiedad/ campo de clase. (Estudiante).

    def getdatosPersonales(self):                                                                                                           # Método/ comportamiento (Clase Estudiante), para la devolución de los datos personales (getter).
        return super().getdatosPersonales() + " Escuela: " + self.escuela                                                                   # Llamada al método (getdatosPersonales), de la clase padre, para añardirle la variable propia de la clase (estudiante), (escuela).

    def estudia(self):
        return "Estoy estudiando"

persona=Persona("Jose", "García", 32)                                                                                                       # Creación del objeto/ Instancia (persona), de la clase padre (Persona).

estudiante=Estudiante("Pedro", "Fernández", 43, "San Javier")                                                                               # Creación del objeto/ Instancia (estudiante), de la clase (Estudiante).

print(persona.getdatosPersonales())                                                                                                         # Impresión en pantalla del método (getdatosPersonales) de la superclase o clase padre (Persona).
print(estudiante.getdatosPersonales())                                                                                                      # Impresión en pantalla del método (getdatosPersonales) de la subclase (Estudiante).

    