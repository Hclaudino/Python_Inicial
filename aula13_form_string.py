'''print(f"utilizar dessa forma {}")'''
# Logo temos:
#f - strings


nome = ('Henique Claudino')
print(f"{nome}")

print('*' * 20)
print('Calculando IMC')
nome = str(input('Digite seu nome: '))
altura = float(input('Digite sua altura: '))
peso = float (input('Diga seu peso: '))
imc = peso / (altura * altura)
print(f"Seu imc é {imc:.2f}") # formantando quantidade casas decimais após a virgulas
print('*' * 20)

'''Exemplo em reais com formatação'''
valor = float(input('Diga um valor: ')) 
print(f'{valor:,.2f}') #formatação para reais