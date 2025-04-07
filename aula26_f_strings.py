'''
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
'''
var = 'ABC'
print(f'{var}')
print(f'{var: >10}.') #PREENCHER OS ESPAÇOS COM 10 CARACTERES A ESQUERDA
print(f'{var: <10}.') #PREENCHER OS ESPAÇOS COM 10 CARACTERES A DIREITA
print(f'{var: ^10}.') #PREENCHER OS ESPAÇOS COM 10 CARACTERES AO CENTRO
print(f'{10000.45898774587:.2f}') 
print(f'O hexadecimal de 1500 é {1500:08x}') 
