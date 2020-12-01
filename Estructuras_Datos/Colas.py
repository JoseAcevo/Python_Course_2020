"""  Queue:
F.I.F.O : First In First Out.
L.I.F.O : Last In First Out.
Priority : Especificar prioridad.
*¿Programación concurrente?
*¿Threats? """


import queue

# F.I.F.O (First In First Out).

miCola = queue.Queue()

miCola.put('Madrid')
miCola.put('Bogotá')
miCola.put('México.DF')

print(miCola.get())
print('A continuación se imprimen los elementos restantes')
for elemento in miCola.queue:
    print(elemento)

# L.I.F.O (Last In First Out)

miCola = queue.LifoQueue()

miCola.put('Madrid')
miCola.put('Bogotá')
miCola.put('México.DF')

print(miCola.get())
print('A continuación se imprimen los elementos restantes')
for elemento in miCola.queue:
    print(elemento)

# PriorityQueue

miCola = queue.PriorityQueue()

miCola.put((3, 'Madrid'))
miCola.put((1, 'Bogotá'))
miCola.put((2, 'México.DF'))

print(miCola.get())
print('A continuación se imprimen los elementos restantes')
for elemento in miCola.queue:
    print(elemento)

# F.I.F.O (First In First Out). Estableciendo límite de parámetros.

miCola = queue.Queue(3)

miCola.put('Madrid')
miCola.put('Bogotá')
miCola.put('México.DF')
print(miCola.full())
print(miCola.get())
print('A continuación se imprimen los elementos restantes')
for elemento in miCola.queue:
    print(elemento)