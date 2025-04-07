'''
enumerate para listas
'''
lista = ['Maria', 'henry','Miguel']
lista.append('Pablo')

#utilizando o star ele inicia a lista no indiece que voce definir (15)
# lista_enumerada = list(enumerate(lista, start=15)) #convertendo o enumerate para uma lista - ou tupla
# print(lista_enumerada)
#lista_enumerada = enumerate(lista) #ele enumera a lista puxando o indice e mostrando o valor de cada indice na frente

# for item in lista_enumerada:
#     print(item) #utilizando o for para mostrar todos os valores (finitos da lista)

# for item in enumerate(lista): #utilizando dessa maneira ele não zera a minha lista
#     a,b = item #sepando em dois valores, a - indice b- valores
#     print(a,b) #caso nao queira  usar  o for posso converter o enumerate para uma lista ou tupla

# for indice, item in enumerate(lista): #melhor forma para mostra os valores e indices da lista
#     print(indice,item)    

for tupla_enumerada in enumerate(lista):
    print('For da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}') #\t ele da uma especie de TAB espaçando os item
        