
'''
for + range
range ~> range(start, stop, step)
'''
# quando eu passo um valor somente eu passo o valor que eu quero que ele pare
#ex: 10 = 0 a 10
#ex: (5, 10) 5 a 9 (valor sempre mostra 1 a menos)
#ex: ( 5 ,10 ,2 ) inicia em 5 vai até 10 pulando de 2 em 2
num = range(0,10,2)

for valor in num:
    print(valor)
    