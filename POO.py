class coche():                                                                      # Creación de una clase (coche).
    
    ruedas=4                                                                        # 
    L_Chasis=2700                                                                   # Propiedades/ atributos de la clase (coche).    
    A_Chasis=1600                                                                   #
    arrancado=False                                                                 # 

    def arrancar(self):                                                             # Método/comportamiento (arrancar) de la clase (coche), destinado a "arrancar" el coche.
        self.arrancado=True                                                         # Cambia el valor de la propiedad (arrancado) al ser llamado el método.

    def estado_coche(self):                                                         # Método/comportamiento (estado_coche)de la clase (coche) destinado a informar sobre el "estado", del coche.
        
        if (self.arrancado):                                                        # Si self(coche).arrancado=True:
            return "El coche está arrancado."                                       # Devolverá el mensaje "El coche está arrancado"
        else:                                                                       # Y si no (else):
            return "El coche no está arrancado."                                    # Devolverá el mensaje "El coche no está arrancado"


citroen=coche()                                                                     # Objeto/ Ejemplar de clase/ instanciar una clase/ instancia de clase.
peugeot=coche()                                                                     # Objeto/ Ejemplar de clase/ instanciar una clase/ instancia de clase.

citroen.arrancar()                                                                  # Llamada al método (arrancar), para su ejecución.

print("El coche tiene un largo de chasis de: "+ str(citroen.L_Chasis)+ "mm")        # Impresión en pantalla de la propiedad (L_Chasis). Utilizando para ello la nomenclatura del punto. (Nombre del objeto .Propiedad/ atributo)
print(citroen.estado_coche())

