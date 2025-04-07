'''
desempacotamento 
'''

nome1, *resto = ['Henrique','Maria','José'] #mesma quantidade de valor e variaveis
_, nome2, *resto = ['Henrique','Maria','José'] #mesma quantidade de valor e variaveis
nome1, *_ = ['Henrique','Maria','José'] #mesma quantidade de valor e variaveis
print(nome1, resto) #empacotou o resto [ maria e josé] e mostrou a variavel nome1 o Henrique

# no lugar do *resto utilziar (underline) *_
# para pegar o segundo valor eu preciso ignorar o primeiro valor logo eu utilizo o underline no lugar do nome1