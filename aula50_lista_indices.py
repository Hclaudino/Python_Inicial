"""
Listas em Python
Tipo list - Mutável *****
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

"""
import os

lista = [10,20,30,40]
lista.append(50)
lista.pop()#remove o ultimo elemento da lista (50)
lista.append(60)
lista.append(70)
lista.append('bbb')
ult_valor = lista.pop(3) #pop retorna um valor
#ult_valor = lista.pop() #pop retorna um valor
print(lista, 'Removido o ultimo valor: ',ult_valor)

# lista [2] =300
# del lista[2] #deletando itens da lista
# print(lista)
# print(lista[2])

# num = lista[2] #pego o valor da lista e jogando em uma variavel
# print(num)