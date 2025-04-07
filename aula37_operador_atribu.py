"""
Operadores de atribuição
 = += -= *= /= //= **= %=
"""

from time import sleep

contador_notas = 0
while contador_notas <= 3:
    contador_notas += 1
    print(contador_notas)
    sleep(1)
print("Acabou")
