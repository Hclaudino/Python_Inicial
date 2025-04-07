# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Digite uma senha: ') #checagem normal
if senha == "123":
    print("Entrou")
else:
    print("Senha incorreta")
    
senha1 = input('Digite uma senha: ') #checar senha incorreta primeiro
if senha1 != "123":
    print("Senha incorreta")
    
senha2 = input('Digite uma senha: ') #che
if not senha2:
    print("Você nao digitou nada")

#not faz a inversão de valor
print(not 0) #True
print(not False) #True
print(not True) #False
