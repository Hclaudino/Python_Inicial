# if / elif      / else
# se / se não se / se não

entrada = input('Você quer entrar ou sair ? ')

if entrada == 'entrar': #if só irar ser executado esse bloco se essa condição for verdadeira
    print("Você entrou no sistema")
elif entrada == 'sair':
    print("Você saiu do sistema")
else:
    print('Você nãop digitou nem entrar e nem sair')
print("Fora dos Blocos")