contador = 0

while contador <= 100:
    contador += 1
    
    if contador ==6: #para pular o laço
        print('Não vou mostar o 06')
        continue
    if contador >=10 and contador <=27: #para pular o laço ocultando o contador
        print('Não vou mostar',contador)
        continue
    
    print(contador)
    if contador ==40:
        break
    
    
print("Acabou")