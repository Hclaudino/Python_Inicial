"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = 'olha so que, frase grande'
#frases = frase.split() #quebra a frase em palavras
# frases = frase.split(',') #quebra a frase em palavras / separar pelo jeito que é escrito
frases = frase.split(',') #quebra a frase em palavras / separar pelo jeito que é escrito

frases_corrigidas = []

for i, frase in enumerate(frases):  #faço a numeração das frases
    frases_corrigidas.append(frases[i].strip()) #strip corta os espaço começo meio e fim

    
    # print(frases)
    # print(frases_corrigidas)
    frase_unidas = '-'.join(frases_corrigidas) #somente strings
    print(frase_unidas)

'''
rstrip = corta da direita
lstrip = corta da esquerda
'''
    
