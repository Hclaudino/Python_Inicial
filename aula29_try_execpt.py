"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
#voce deve sempre tratar o input do usuario para que não haja erros

c = input('Me de um número para duplicar: ')
try:
    d = float(c)
    mm = (d*2)
    print("FLOAT", d)    
    print(f"o Dobro de {c} é igual a {mm}")
except:
    print('isso não é um numero')



'''n = input("Digite um número para que eu possa duplicar: ")
print(n.isdigit()) #se o usuario digitar somente numero ele indica True ou False
nf = float(n)
m = (nf*2)
print(f"o dobro de {n} é igual a {m:.2f}")

n = input("Digite um número para que eu possa duplicar: ")
if n.isdigit():
    nf = float(n)
    m = (nf*2)
    print(f"o dobro de {n} é igual a {m:.2f}")
else:
    print("Você digitou um valor errado")

'''
'''
print(1234) #mostra o erro para entender o que é exeção 
print(456)
int('a') #isso é exeção '''