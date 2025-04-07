# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')
entrada = input('[E]ntrar [S]air: ')
senha = input('Digite uma senha: ')
senhap = '123456'
#separando com () para avaliar a condição
if (entrada == 'E' or entrada == 'e') and senha == senhap: #adicionando porta OR para aceitar 'E' ou 'e'
    print("Entrar")
else:
    print("Sair")

print(0 or False or False or 'abc')
print(True or False or False or 'abc')
print(False or True)

senh = input('Diga sua senha ') or 'Sem senha'
print(senh)

