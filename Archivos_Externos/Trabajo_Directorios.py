import os
import io
#os.makedirs('prueba_Directorio')

os.chdir('prueba_Directorio')
primer_archivo = open('primerArchivo.txt', 'w')
primer_archivo.write('The design of all built-in operating system dependent modules of Python is such that as long as\n'
                     'the same functionality is available, it uses the same interface; for example, \n'
                     'the function os.stat(path) returns stat information about path in the same format \n'
                     '(which happens to have originated with the POSIX interface).')
primer_archivo.close()

print(os.getcwd())

