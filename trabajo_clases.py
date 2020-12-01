class Coche:
    ruedas = 4
    largoChasis = 2560       # Propiedades/características
    anchoChasis = 1520

    def arranque(self):      # Método o comportamiento de la clase (Coche)
        pass


Citroen = Coche()            # Ejemplar de clase/ Ejemplarizar una clase/ objeto de clase.

Mitsubishi = Coche()            # Ejemplar de clase/ Ejemplarizar una clase/ objeto de clase.


Citroen.altura = 1220        # Asignación de una nueva propiedad/ característica utlizando para ello la nomenclatura del punto.

print(Citroen.ruedas)        # Acceso al valor de la propiedad utilizando para ello la nomenclatura del punto.

