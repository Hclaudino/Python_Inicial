"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade """

condicao = True
pass_if = None
if condicao:
    pass_if = True
    print("Faça Algo")
else:
    print("Não faça algo")
    
if pass_if is None:
    print(" Não passou No IF")
else:
    print(" passou No IF")
    
    
'''print(pass_if, pass_if is not None) 
print(pass_if, pass_if is None) #is not sempre invertendo as lógicas'''