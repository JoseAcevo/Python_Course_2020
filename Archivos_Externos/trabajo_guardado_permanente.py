import pickle                                                               # Importación de la biblioteca pickle.


class Persona:                                                              # Creación de la superclase / Clase padre (Persona).

    def __init__(self, nombre, genero, edad):                               # Método constructor de la clase Persona.
        self.nombre = nombre                                                #
        self.genero = genero                                                # Campo/ variable de clase.
        self.edad = edad                                                    #
        print(f"Se ha creado un nuevo objeto/persona llamada: {self.nombre}") # Impresión en pantalla de la confirmación de la creación del objeto.

    def __str__(self):                                                      # Método STR con el cual se convierte a string la información de un objeto.
        return f"{self.nombre} {self.genero} {self.edad}"                   # Devolución de la información pasada por parámetros al método constructor, aplicándole el formato correspondiente.


class ListaPersonas:                                                        # Creación de una nueva clase (Lista_Personas).

    personas = []                                                           # Creación de una lista (personas), para almacenar los datos, que luego volcaremos en el FicheroExterno.

    def __init__(self):                                                     # Creación del método consructor de la clase (Lista_Personas).

        lista_personas = open("FicheroExterno.pckl", "ab+")                 # Cración de una variable (EN MEMORIA), encargada de crear y abrir el fichero externo en el cual volcaremos los datos de la lista (Personas).
        lista_personas.seek(0)                                              # Recolocación (seek) del cursor en la posición cero en el fichero Externo, para que posteriormente podamos leer e imprimir la info almacenada en él.

        try:  # Intenta:
            self.personas = pickle.load(lista_personas)                                              # Cargar los datos almacenados en la variable (EN MEMORIA(lista_personas)) en la lista (pesonas=[]), para poder leerla.
            print(f"Se han cargado {len(self.personas)} personas desde el FicheroExterno.")           # Confirmación de la carga de la información en la lista (personas =[]). aplicándole el formato correspondiente junto al método (len).

        except:  # Excepto:
            print("Se acaba de añadir un nuevo elemento al FicheroExterno")                           # Si es la primera vez que se ejecuta el programa el fichero externo estará vacío, en ese caso se imprimirá un mensaje de advertencia.

        finally:  # Finalmente:
            lista_personas.close()                                                                    # Cerramos la variable EN MEMORIA (lista_personas).
            del lista_personas                                                                        # Borramos de la MEMORIA la variable (lista_personas).

    def agregarPersonas(self, p):                                                                     # Método encargado de agregar objetos/ personas(p).
        self.personas.append(p)                                                                       # Utilizamos el método (append), para añadir objetos/personas a la lista (personas=[]).
        self.guardado_personas_FicheroExterno()                                                       # Llamada al método (guardado_personas_FicheroExterno).

    def mostrarPersonas(self):                                                                        # Método encargado de mostrar la info almacenada en la lista (personas=[]).

        for p in self.personas:                                                                       # Bucle for encargado de recorrer la info de la lista (personas=[]).
            print(p)                                                                                  # Impresión de la info almacenada en la lista (personas=[])

    def guardado_personas_FicheroExterno(self):                                                       # Método encargado de guardar la info en el FicheroExterno.
        lista_personas = open("FicheroExterno.pckl", "wb")                                            # Creamos/abrimos la (lista_personas) en memoria en modo (escritura binaria (wb)).
        pickle.dump(self.personas, lista_personas)                                                    # Volcado (.dump) de la info guardada en la lista (personas=[]) en el FicheroExterno a través de la variable EN MEMORIA (lista_personas).
        lista_personas.close()                                                                        # Cerrado de la variable EN MEMORIA (lista_personas).
        del lista_personas  # Borrado de la variable (lista_personas), de la MEMORIA.

    def mostrar_info_FicheroExterno(self):                                                            # Método encargado de mostrar la info almacenada en el FicheroExterno.
        print("La información almacenada en el fichero externo es la siguiente: ")                    # Impresión en pantalla de dicha info.
        for p in self.personas:                                                                       # Bucle for encargado de recorrer la info guardada en la lista (personas=[]).
            print(p)  # Impresión


P = Persona('Raquel', 'femenino', 23)                                                                 # Creación un objeto (p) de clase (Persona).
mi_lista = ListaPersonas()                                                                            # Instanciación de la clase (Lista_Personas), para poder crear objetos de esa clase.
mi_lista.agregarPersonas(P)                                                                           # Uso del objeto (mi_lista) de la clase (Lista_Personas), para llamar al método (agregarPersonas) y poder pasarle el objeto previamente creado (p), por parámetro.
mi_lista.mostrarPersonas()                                                                            # Uso de la instancia (mi_lista), para mostrar la info almacenada en la lista (personas=[])
mi_lista.mostrar_info_FicheroExterno()                                                                # Uso de la instancia (mi_lista), para mostrar la info almacenada en el FicheroExterno.

# 1.- Creamos la instancia de tipo Lista_Personas: 
# mi_lista=Lista_Personas().

# 2.- Creamos el objeto (p) de la clase (Persona), con sus valores a pasar al constructor por parámetro.
# p = Persona("Ana", "femenino", 19).

# 3.- Añadimos el objeto creado (p) a la lista (personas=[]) y lo guarda en el FicheroExterno.
# mi_lista.agregarPersonas(p).
