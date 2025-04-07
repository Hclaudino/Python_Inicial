# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 6 7
#  h e n r i q u e
# -8-7-6-5-4-3-2-1
# nome = 'henrique'
# print(nome[2])
# print(nome[-4])
# print('vio' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('ino' not in nome)
# print('zero' not in nome)

nome = 'henrique' 
print(nome[2]) #acessar a letras no índice utilizando []
print(nome[0]) #acessar a letras no índice utilizando []
print( 'n' in nome) #checagem de letras
print( 'z' in nome) #checagem de letras
print( 'que' in nome) #checagem de palavras
print( 'que' not in nome) #checagem de palavras
print( 'hc' not in nome) #checagem de palavras inversas
print( '-' *25) #

n = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar?')

if encontrar in n:
    print(f"Está no nome! ")
else:
    print('Não está no nome! ')
    