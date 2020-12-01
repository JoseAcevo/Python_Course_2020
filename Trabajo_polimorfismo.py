class Persona():
    def hablar(self):
        return "habla Antonio"

class Trabajador(Persona):
    def hablar(self):
        return "Habla María"

class Director(Trabajador):
    def hablar(self):
        return "Habla Ana"

Antonio=Persona()
Maria=Trabajador()
Ana=Director()

print(Antonio.hablar())
print(Maria.hablar())
print(Ana.hablar())

def hazles_Hablar(listadeelementos):
    for Persona in listadeelementos:
        print(Persona.hablar())




print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<------------------------------------------------------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


listaPersonas=[Antonio, Ana, Maria]
hazles_Hablar(listaPersonas)

