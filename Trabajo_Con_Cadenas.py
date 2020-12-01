#nusuario=(input("Introduzca su usuario, por favor: "))
#print("El usuario introducido es: ", nusuario.capitalize())

edad=(input("Introduzca su edad, por favor: "))

while(edad.isdigit()==False):
    print("El valor introducido NO es correcto ")
    edad=(input("Inténtelo de nuevo por favor: "))

if(int(edad)<18):
    print("No puede pasar")
else:
    print("Puedes pasar")

