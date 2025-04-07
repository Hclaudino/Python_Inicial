"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

"""
lista = [10,20,30,40]
lista.append('Henrique')
nome = lista.pop()#removi o ultimo item
lista.append(1234)#acresci um item no final da lista
del lista[-1] # usando o indíce invertido ele deleta  o ultimo item da lista (sempre vai ser o ultimo item da lista)
lista.insert(0,5) #precisa de dois valores sendo : qual indice (0) e qual o valor voce colocara (5)

print(lista)