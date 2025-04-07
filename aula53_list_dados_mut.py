"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Henrique', 'Katia'] #naõ estou copiando, só estou fazendo os valores apontarem para o mesmo valor 'Henriqu' 'katia'
lista_b = lista_a.copy() #fazendo dessa forma não altera a lista (utilizando o copy)

lista_a[0] = 'Qualquer Coisa' #mesmo mudando a lista_a, ele muda o valor printando a lista_b
print(lista_b)
print(lista_a)

# nome = 'Henrique' #
# nom = nome
# nome = 'João'
# print(nome)
# print(nom)