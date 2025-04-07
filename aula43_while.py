'''frase = ' o python é uma linguagem de programação ' \
    'multiparadigma.' \
    ' Python foi criado por Guido Vans Rossum'.lower()
    
print(frase.count('python')) # conta a quantidade das palavras na frase.'''

frase = ' o python é uma linguagem de programação ' \
    'multiparadigma.' \
    ' Python foi criado por Guido Vans Rossum'.lower().strip()
i = 0  
ap = 0
app = ''  
while i < len(frase):   
    
    letra = frase[i]
    
    if letra == ' ':     
        i += 1      #colocando aqui dentro pois gera loop infinito tudo que coloco depois do continue
        continue
    
    qnt = frase.count(letra)
    if ap < qnt:
        ap = qnt
        app = letra
    
    
    i += 1 
    
print(f'A Letra que apaceu mais vezes foi {app} aparecendo {ap} ')

#contagem de qu