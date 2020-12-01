
#Métodos dunder (double underscore).
#class Persona ():
    
    #def __init__(self, nombre, apellido, edad):
        #self.nombre=nombre
        #self.apellido=apellido
        #self.edad=edad

    #def __str__(self):
        #return "Datos de la persona: \n"+self.nombre+"\nApellido: "+self.apellido+"\nEdad: "+ str(self.edad)
    
    #def __repr__(self):                                                                                                            # Método repr, identifica al objeto de forma inequívoca, NO ambigua.
        #return "Datos de la persona: \n"+self.nombre+"\nApellido: "+self.apellido+"\nEdad: "+ str(self.edad)

#p1=Persona( "jose", "Acevo", 18)
#print(p1)

#class Persona():
   
    #def __init__(self, **kwargs):
        #elementos=kwargs.items()

        #for clave, valor in elementos:
            #print(clave, " ", valor)

#p1=Persona(nombre="Juan", Apellido="Díaz", Edad=18)

#import datetime

#hoy=datetime.date.today()

#print(repr(hoy))                                                                                                                  # Método repr, identifica al objeto de forma inequívoca, NO ambigua.

# Mëtodo (__len__)

class Agenda():
    
    def __init__(self):
        self.mi_agenda={}
    
    def agregarPersonas(self, nombre, telefono):
        self.mi_agenda[nombre]=telefono

    def __len__(self):                                                                                                            # Método dunder (len) nos devuelve la longitud de (mi_agenda)
        return len(self.mi_agenda)

agenda_personal=Agenda()
agenda_personal.agregarPersonas("Juan", "2049380925")
agenda_personal.agregarPersonas("Maria", "489570392")

print(len(agenda_personal))


        






























