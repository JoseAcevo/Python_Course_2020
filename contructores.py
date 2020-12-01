#Ejemplo con métodos/propiedades sin encapsular.

#class persona():                                                    # Creación de una clase (Persona).
    
    #nombre=""
    #apellido=""                                                     # Propiedades o atributos de la clase (persona).
    #edad=0
    #genero="No definido"

    #def __init__(self, nombre, apellido, edad, genero):             # Método constructor, para iniciar las propiedades o atributos en todos los objetos que pertenezcan a la misma clase (persona).

        #self.nombre=nombre
        #self.apellido=apellido
        #self.edad=edad
        #self.genero=genero

    #def habla(self):                                                # Mëtodo (habla)

        #return "La persona cuyo nombre es ", self.nombre, "está hablando"


    #def camina(self):
        
        #return "La persona cuyo nombre es ", self.nombre, "está caminando"

    #def getDatos(self):
        
        #return "Nombre", self.nombre, "Apellido", self.apellido, "Edad",str(self.edad), "Género", self.genero

#p1=persona("Jose", "Martinez", 32, "Masculino")                 #Creación de un objeto/instancia, perteneciente a la clase persona, con una serie de valores para sus propiedades.
#print(p1.getDatos())                                            # Acceso a la información utilizando el método (Get datos)


#Ejemplo con métodos/propiedades encapsuladas. utilizando también los "métodos de acceso", setters y getters.
#Encapsulado con un sólo guión bajo(_nombre): La propiedad se podrá utilizar en la propia clase y en todas las que hereden de esa propiedad.
#Encapsulado don dos guiones bajos(__nombre): La propiedad sólo se podrá utilizar en la propia clase.
#Utilizando también los "métodos de acceso", setters y getters:
#Setters: Establecen los valores en las propiedades.
#Getters: Accede a que valor hay almacenado en una propiedad en concreto.

class persona():                                                    # Creación de una clase (Persona).
    
    __nombre=""
    apellido=""                                                     # Propiedades o atributos de la clase (persona).
    __edad=0
    genero="No definido"

    def __init__(self, nombre, apellido, genero):                   # Método constructor, para iniciar las propiedades o atributos en todos los objetos que pertenezcan a la misma clase (persona).

        self.__nombre=nombre
        self.apellido=apellido
        self.genero=genero
    
    def setEdad(self, Age):                                         #Uso del método de acceso (setter), para acceder al parámetro edad desde fuera de la clase.
        
        if Age<0 or Age>100:
            print("Parámetro incorrecto")
        
        else:
            self.__edad=Age
            return self.__edad

    def habla(self):                                                # Mëtodo (habla)

        return "La persona cuyo nombre es ", self.__nombre, "está hablando"


    def camina(self):
        
        return "La persona cuyo nombre es ", self.__nombre, "está caminando"

    def getDatos(self):                                           # Uso del método de acceso (Getter), para que nos devuelva la información de un objeto del tipo persona.
        
        return "Nombre", self.__nombre, "Apellido", self.apellido, "Edad",str(self.__edad), "Género", self.genero

p1=persona("Jose", "Martinez", "Masculino")                       #Creación de un objeto/instancia, perteneciente a la clase persona, con una serie de valores para sus propiedades.
p1.setEdad(21)
print(p1.getDatos())                                              # Acceso a la información utilizando el método (Get datos)

# Ver video otra vez.