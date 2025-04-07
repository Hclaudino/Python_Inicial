'''Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
'''
var = 'Olá Mundo'
print(var[5])
print(var[4:]) # : indica o fatiamento
print(var[0:5]) # : indica o fatiamento
print(len(var[0:5])) #função len indica quantos caracteres está sendo usado
print(var [0:len(var):4]) #o :2 no final é a quantia de caracteres que ira ser pulado
print(var [::-1]) #Inverte a contagem da string
