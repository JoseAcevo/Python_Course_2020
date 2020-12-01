"""( Set {...........} ): Colección no ordenada de elementos que NO admite repetición:
.-No admite indexación.
.-No registran la posición del elemento.
.-No registran órden de inserción."""

sistema_solar = "Mercurio,Venus,Tierra,Marte,Júpiter,Saturno,Urano,Neptuno,Plutón" # Linea común, no comentar nunca.

planetas=set()                                                              # Creación (set) programa versión1.
#planetas=set(sistema_solar)                                                # Creación (set) progarma versión2.

for planeta in sistema_solar.split(","):                                    # Bucle For para programa versión1
    planetas.add(planeta)                                                   # Definición bucle for para programa version1

print(planetas)                                                             # Linea común ambas versiones.
print(len(planetas))                                                        # Linea común ambas versiones.




