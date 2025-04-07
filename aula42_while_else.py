#while - else

string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]
    
    if letra == ' ':
        break
    #break no while não executa o while
    print(letra)
    i += 1
else:
    print("O Else foi executado")
print("Fora do while")    