'''
Repetições 
while (enquanto)
Executa uma ação enquanto uma condições for verdadeira
Loop infinito quando o código não tem fim
enquanto a condição for True ele entra no while, quando for false ele não executa
'''
from time import sleep 
contador = 0

while contador <= 3:
    contador = contador + 1
    print(contador)
    sleep(1) # import time ( deixando mais devagar para aprendizagem)
print("Acabou")