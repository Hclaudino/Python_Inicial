#exemplo de comparação de valores com utilização de if

p1 = input('Digite um primeiro valor: ')
p2 = input('Digite um segundo valor: ')
if p1 > p2:
    print(f'o primeiro valor é maior {p1}')
elif p2 > p1:
    print(f"o Segundo valor é maior {p2} ")
elif p1 == p2:
    print(f"Os Dois valores são iguais {p1} = {p2}")
    
'------------------------------------------------------'
#utilizando verifacação de código para não haver erros de digitação de número
n1 = input('Digite um valor de um número: ')
n2 = input('Digite um valor de um número: ')
fn1 = float(n1)
fn2 = float(n2)
if fn1 > fn2:
    print(f"o Valor {fn1} é maior que {fn2} ")
else:
    print(f"o Valor {fn2} é maior que {fn1} ")
    

