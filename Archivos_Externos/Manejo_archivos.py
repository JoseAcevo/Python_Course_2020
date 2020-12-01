# Fases en la manipulación de archivos externos.
# Creación
# Apetura
# Manipulación
# Cierre

# Creación/ apertura de un archivo externo en modo escritura (w).

# from io import open                                                                        # Importación del método open del módulo IO.
# archivo_texto=open("archivo.txt", "w")                                                     # Creación y apertura del archivo externo (archivo.txt), en modo escritura (w), mediante la variable en memoria (archivo_texto)
# frase="Estupendo día para rehacer todo el curso de python.."                               # Info a incluir en el archivo externo (en este caso, una simple frase)
# archivo_texto.write(frase)                                                                 # Uso de la variable en memoria (archivo_texto), para escribir la info en el archivo externo.
# archivo_texto.close()                                                                      # Cierre EN MEMORIA, de la variable (archivo_texto) encargada de crear y abrir el archivo externo (archivo.txt)


# Creación y apertura de un archivo externo en modo lectura (r).

# from io import open                                                                         # Importación del método open del módulo IO.
# archivo_texto = open("archivo.txt", "r")                                                      # Creación y apertura del archivo externo (archivo.txt), en modo lectura (r), mediante la variable en memoria (archivo_texto).
# texto=archivo_texto.read()                                                                  # Creación de una variable (texto), para poder leer la info almacenada en la variable en memoria (archivo.texto).
# archivo_texto.close()                                                                       # Cierre de la variable en memoria (archivo_texto)
# print(texto)                                                                                # Impresión en pantalla de la info almacenada en la variable (texto).


# Readlines. (Permite leer la info almacenada en un archivo, linea a linea y almacenarla en una lista).
  
# from io import open                                                                           # Importación del método open del módulo IO.
# archivo_texto=open("archivo.txt", "r")                                                        # Creación y apertura del archivo externo (archivo.txt), en modo lectura (r), mediante la variable en memoria (archivo_texto)
# lineas_texto=archivo_texto.readlines()                                                        # Creación de una lista (mediante el método (.readlines) llamada (lineas_texto), para poder guardar en ella la info almacenada en la variable abierta en memoria, (archivo_texto) para poder manipularla.
# archivo_texto.close()                                                                         # Cerrado de la variable (EN MEMORIA)
# print(lineas_texto)                                                                           # Impresión en pantalla de la info almacenada en la lista.

# Adicción de información al archivo externo (.append)

# from io import open                                                                           # Importación del método open del módulo IO.
# archivo_texto=open("archivo.txt", "a")                                                        # Apertura de variable en memoria (archivo_texto), para la posterior apertura del archivo externo (archivo.txt) en modo de adicción (.append)
# archivo_texto.write("\n despues de habermelo cargado ayer entero")                            # Apertura de la variable en memoria (archivo_texto),para poder añadir info al archivo.txt mediante el método (.write).
# archivo_texto.close()                                                                         # Cerrado de la variable en memoria.

# Reposicionamiento del cursor (.seek) vs (.read).

# from io import open                                                                           # Importación del método open del módulo IO.
# archivo_texto=open("archivo.txt", "r")                                                        # Creación y apertura del archivo externo (archivo.txt), en modo escritura (w), mediante la variable en memoria (archivo_texto)
# print(archivo_texto.read())                                                                   # Impresión en consola de toda la info almacenada en la variable (archivo_texto(en memoria)), ya que no le  especificamos límite alguno.
# archivo_texto.seek(11)                                                                        # Recolocación del cursor en un carácter determinado (11)
# archivo_texto.seek(len(archivo_texto.read())/2)                                               # Recolocación del cursor en la mitad del (archivo_texto), usamos para ello, el método (len), para conocer la longitud total y al final le pedimos la mitad (/2).
# print(archivo_texto.read())                                                                   # Impresión en consola de la info almacenada en la variable (archivo_texto(en memoria)), hasta el carácter que le digamos (11, en este caso).



# (.seek), sólo reposiciona el cursor en el lugar en que le especificamos.
# (.read), realiza una lectura hasta el carácter que le indiquemos.
# (.readline), reposicionamiento del cursor al final de la primera línea (lee la info línea a línea.)


# Apertura del fichero en modo lectura+escritura
from io import open                                                                           # Importación del método open del módulo IO.
archivo_texto=open("archivo.txt", "r+")                                                       # Creación y apertura del archivo externo (archivo.txt), en modo lectura + escritura (r+), mediante la variable en memoria (archivo_texto)
#archivo_texto.write("Comienzo del texto")                                                    # Sobreescritura de la primera línea de archivo.txt.
#print(archivo_texto.readlines())                                                             # Impresión del archivo.txt en forma de lista (.readlines).
linea_nueva=archivo_texto.readlines()                                                         # Creación de una lista (linea_nueva) mediante el método (.readlines) en la variable en memoria(archivo_texto) y por lo tanto, en el (archivo.txt (externo)).
linea_nueva[1]=" Esta linea ha sido incluída a posteriori"                                    # Inclusión de una nueva línea en la lista previamente creada (archivo_texto.readlines) en una posición determinada[1].
archivo_texto.seek(0)                                                                         # Recolocación del cursor en la posición (0)
archivo_texto.writelines(linea_nueva)                                                         # Escritura de la nueva línea mediante el método (.writelines)
archivo_texto.close()                                                                         # Cerrado de la variable en memoria (archivo_texto).

