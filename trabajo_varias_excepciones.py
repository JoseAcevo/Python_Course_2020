#Instrucciones (Try and Except)

def divide ():

    try:
         op1=(float(input("Introduzca un número: ")))
         op2=(float(input("Introduzca un segundo número: ")))

         print("El resultado es: " + str (op1 / op2))

    except ZeroDivisionError:
        print("Operación no válida.")

    except ValueError:
        print("Valor introducido no válido.")


    finally:
        print("Se ha intentado ejecutar la función en su totalidad")                                           #Instrucción (Finally): Siempre se ejecutará lo que haya en su interior.
    

divide()

print("Cálculo finalizado")















