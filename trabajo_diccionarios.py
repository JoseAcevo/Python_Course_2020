#Mi_Marga = {

 #   "Nombre" : "Margarita",

 #   "Apellido" : "Filosa",

 #   "Alias" : "cuchillos",

 #   "Padres" : ["María Chaira", "Carlos Cortez"],
    
 #   "Edad" : 55,
    
 #   "Genero " : "Femenino",
    
 #   "Estado civil" : "Soltera",
    
 #   "Hijos" : "Ninguno/a",
    
 #   "Mascotas" : "Gatos",
    
 #   "Nombres_mascotas" : ["Mango", "Tito"]
    
 #   }


#print(Mi_Marga["Apellido"])                                                                                        # Impresión en consola del valor de una clave

#print(Mi_Marga ["Padres"] [0:2])                                                                                   # Impresión en consola de los elementos que forman una lista, en el interior de un diccionario indicando a su vez los índices que queremos imprimir.

# Mi_Marga["Ingresos"] = "$16000"                                                                                   # Adicción de una nueva pareja clave/valor

#Mi_Marga["Ingresos"] = "20000"                                                                                      # Modificación del valor de una clave en concreto.

# Mi_Marga["Salario"] = Mi_Marga.pop("Ingresos")                                                                    # Corrección de una clave (.pop)

# del(Mi_Marga["Nombre"])                                                                                           # Eliminación de una clave y su valor.

#............................................................................................................................................

#Métodos en los diccionarios. (.get).

#print(Mi_Marga.get("Nombre","Valor por defecto si la clave no tiene uno"))                                         # Obtención del valor de una clave.

#el_nombre = Mi_Marga.get("Nombre","No tiene nombre")                                                               # Asignación de una clave a una variable para obtener su valor. Si la clave no existiese mostraría el valor "no tiene nombre"

#print(el_nombre)

#Métodos en los diccionarios. (.setdefault).

dict = {"Nombre": "Zara", "Edad": 27}

print ("Valor : %s" % dict.setdefault("Edad", None))
print ("Valor : %s" % dict.setdefault("Raza", None))








#...................................keys / Values.....................................................................................................................

#Keys = claves
#values = Valores

#print (Mi_Marga.keys())
#print (Mi_Marga.values())

#.................................Ordenar diccionarios.
# Se puede hacer utilizando un bucle (For).
#print(Mi_Marga)







  





