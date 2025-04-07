'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
append - Adiciona um item ao final
insert - Adiciona um item no índice escolhido
pop - Remove do final ou do índice escolhido
del - apaga um índice   clear - limpa a lista
extend - estende a lista
+ - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
'''
#fazer concatelnação de listas / juntar duas lista em uma terceira lista.
lista = [10,20,30,40] 
lista1 = [15,25,35,45]
lista2 = lista + lista1
lista3 = lista.extend(lista1) #gera um none = não valor = faz a ação mais nao me entrega um valor de volta/
#mexendo diretamente na lista extendendo para a lista1
print(lista3) 
print(lista) #mostra a extensão da lista = lista1 + lista