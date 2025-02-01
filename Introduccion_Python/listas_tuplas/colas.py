"""
Colas
"""
cola = []

cola.append(1)
cola.append(2)
cola.append(3)
cola.append(4)

print(cola)

# el primero en entrar es el primero en salir
cola.pop(0)

print(cola)

# Crear una cola en python 
from collections import deque

colas = deque()
print(colas)

colas.append(1)
colas.append(2)
colas.append(3)
colas.append(4)

print(colas)

# eliminar el primer elemento de una cola en deque
colas.popleft()

print(colas)