"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
Exiba:
Seu nome é {nome}
Seu nome invertido é {nome invertido}
Seu nome contém (ou não) espaços
Seu nome tem {n} letras
A primeira letra do seu nome é {letra}
A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
exiba "Desculpe, você deixou campos vazios."
"""


nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
'''varn = str(nome)'''
'''vari = int(idade)'''

if nome and idade:
    print(f"Seu nome é: {nome}")
    print(nome[::-1])
    if ' ' in nome:
        print("Seu nome há espaços")
    else:
        print("Não há espaços em seu nome")
    print(len(nome))
    print(nome[0])
    print(nome[-1])
else:
    print("Desculpa você deixou campos vazios")
    
    