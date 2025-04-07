# iterando strings com while

nome = 'Henrique'
tamanho = len(nome)
indice = 0 # contador de indice
fig = '' # contador do que ira ser acrescido
while indice < len(nome): #estrutra while em cima do indice e len
    
    letra = nome[indice] #criar nova variavel letra sendo igual variavel nome e buscar indice
    fig += f'*{letra}'  #variavel fig do contador contando letra do nome
    indice += 1 #contando o indice
    
fig += '*' #adicionando o que quer no indices separados
    
print(fig) # mostrando o resultado final