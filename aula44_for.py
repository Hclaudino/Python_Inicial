texto = 'python'

i = 0
string = len (texto)
while i < string:
    print(texto[i], i)
    
    i +=1
    
print("-" * 25)
#while utilizando para quando não sei quantas vezes eu preciso refazer algo

senha_s = '1234'
senha_d =''
repeticoes = 0
while senha_s != senha_d:
    senha_d = input(f'Digite a senha ({repeticoes}x): ')
    repeticoes += 1
print(repeticoes)
print("Aquele laço acima pode ser infinito")
print("-" * 25)


text = 'python'
novo_tx =''
for c in text:
    novo_tx += f'*{c}'
    print(c)
print(novo_tx + '*')

