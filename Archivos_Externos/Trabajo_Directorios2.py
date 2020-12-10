import os
#import io

#os.makedirs('Archivos_Externos/PracticaDirectorio2')                  # Creación de un directorio
#os.chdir('Archivos_Externos/')                      # Nos movemos al directorio creado previamente.
#os.chdir('Archivos_Externos/PracticaDirectorio2')
#os.makedirs('PracticaDirectorio3')
#os.rename('Ejemplo.txt', 'Archivo a eliminar.txt')                    # Renombrar el archivo.
#os.rename('Ejemplo2.txt', 'y este tambien')
#os.remove('Archivo a eliminar.txt')                                   # Eliminación de un archivo.
#os.chdir('../')                                                         # Nos movemos un nivel hacia atras en la jerarquía de carpetas.
#os.rmdir('PracticaDirectorio2')                                         # Eliminación del directorio.
#archivo_externo=open('Ejemplo2.txt', 'w')
"""
archivo_externo.write('This Module provides a portable way of using operating system dependent functionality. \b'
                      'If you just want to read or write a file see open(), if you want to manipulate paths,\b'
                      ' see the os.path module, and if you want to read all the lines in all the files\b'
                      ' on the command line see the fileinput module. For creating temporary files and directories\b'
                      ' see the tempfile module, and for high-level file and directory handling see the shutil module.')
"""
#archivo_externo.close()
#print(os.getcwd())  # Muestra el directorio en el que nos encontramos.
#print(os.listdir('./'))

lista_archivos = os.listdir('./')
for archivo in lista_archivos:
    if archivo == 'Tirar.py':
        os.remove(archivo)

    else:
        print('El archivo solicitado no existe')