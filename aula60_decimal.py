"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
""" 
import decimal #Utiliza para número de ponto flutuantes com muitas casas decimais

n1 = decimal.Decimal('0.1') #coloco como STRING para retornar o valor correto ''
n2 = decimal.Decimal('0.7')
num = (n1+n2)
print(num) #ele gera um número impreciso 0.799999
print(f'{num:.2f}') #colocando ele assim ele me gera um valor arredondado (retorna STRING)
print(round(num, 2)) #utilizando ele eu escolho a variavel e coloco a quantidade de casas que eu precisaria (RETORNA NÚMERO FLOAT) ELE ARRENDONDA

