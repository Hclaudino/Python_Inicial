
print('*' *15)
print('Calculando IMC')
nome = str(input('Digite seu nome: '))
altura = float(input('Digite sua altura: '))
peso = float (input('Diga seu peso: '))
imc = peso / (altura * altura)
print(f"Seu imc é {imc}")
