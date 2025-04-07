"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Henrique'
preço = 1000.955898
variavel = '%s, o preço é R$%.2f' % (nome,preço) 
print(variavel)
print('o hexadecimal de %d é %04x' % (1750,1750)) #transforma para hexadecimal - para completar as casas colocar 0 e quantia de casa 4 - 8