
'''Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
'''
c = input('Digite um número: ')
try:
    d = int(c) #formatando os dados para conversões no try
    mm = d % 2 
    if mm == 0:
        print("Você digitou um número par!")
    elif mm == 1:
        print("Você digitou um número impar")
except:
    print("Você não digitou um número inteiro Tente novamente")

"""

Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
a = input("Digite a hora em número inteiros: ")
try:
    d = int(a)
    if d >= 0 and d <= 11:
        print("Bom dia")
    elif d >= 12 and d <= 17:
        print("Boa Tarde")
    elif d >= 18 and d <= 23:
        print('Boa Noite')
    else:
        print("Não conheço essa hora! ")
except:
    print("Você não digitou a hora em números inteiros")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu primeiro nome: ')
nom = len(nome)  #para poder fazer a conversão de str para números int na contagem do nome
if nom >= 2:
    if nom <= 4:
        print("Você tem um nome curto")
    elif nom >= 5 and nom <= 6:
        print('Você tem um nome normal')
    elif nom > 6:
        print("Você tem um nome grande")
else:
    print("Digite mais que uma letra")

