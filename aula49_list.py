"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +

"""

string = 'ABCDE' #CADEIA DE CARACTÉRES (len) (indices [3] )
# lista = [] #criação de lista com colchetes / tipo mutavél, dentro da lista pode conter outra lista
#--------0-----1----------2-----3----4 ///// acessar por indices porém o item inteiro
lista = [123, 'Henrique', True, 1.2, []]
lista[1] ='Katia' #atribuir outra valor para alterar
print(lista) #ele altera o valor na própria lista
print(lista[1], type(lista[1])) #ele mostra somente um item da lista / posso checar  o tipo do items 02 da lista


# print(bool([]))
# print(lista,type(lista))

