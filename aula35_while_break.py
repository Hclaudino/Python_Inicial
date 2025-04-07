'''
Repetições 
while (enquanto)
Executa uma ação enquanto uma condições for verdadeira
Loop infinito quando o código não tem fim
'''

while True:
    nome = input('digite seu nome: ')
    print(f"Seu nome é {nome} ")
    
    if nome == 'sair':
        break
    
print("Acabou")