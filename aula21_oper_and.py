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
senha = input('Digite sua senha:')
senhap = '15'
#if condição 
if entrada == 'E' and senha == senhap:
    print("Entre")
else:
    print("Sair")
#avaliação de curto circuito    
print(True and True and True)
print(True and False and True)
print(True and 0 and True)
print(bool(''))