"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.

"""
import os

lista = []

while True:
    print('Selecione uma opção: ')
    opcao = input('[i]nserir [a]pagar [l]istar :') #faz o usuario decidir o que fazer
    
    if opcao == 'i':
        os.system('cls') #apaga o console
        valor = input('Digite o valor: ')
        lista.append(valor) #adiciona na lista o que o usuario indicou
    elif opcao == 'a':
        indices_str = input('Digite o indice a ser apagado: ')
        try:
            indice = int(indices_str) #transforma para inteiro
            del lista[indice] #apaga da lista o indice
        except ValueError: #erro de valor
            print('Por favor digitar um número inteiro') #caso de o ValueError printar isso!
        except IndexError: #erro no index 
            print('Não existe esse valor na lista')  #
        except Exception: #erro desconhecido
            print('Erro desconhecido') #erro desconhecido
    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0: #fazendo a contagem e leitura dos indices do len da lista 
            print('Nada para listar')
        for i,valor in enumerate(lista): #faz a numeração do indices do enumerador de lista
            print(i,valor) #mostra o valor do enumerador
    else:
        print("Por favor digite i , a , l")  #serve para pedir que o usuario digite a letra corretaS