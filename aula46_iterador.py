"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
#exemplo for letra in text
text1 = 'Henri'
for letra in text1:
    print(letra)
print('/////'*5)


text = 'Henrique' #iteravel
iterador = iter(text) #interador
while True:
    try:
        print(next(iterador))
    except  StopIteration:
        break
print('*'*25)    

texto = 'Henrique'.__iter__() # () ele retorna uma ação precisa dos ()
texto = iter('Henrique') #função para iter acima

print(next(texto)) #funçaõ next igual a next()

# print(texto.__next__())# função next ele entrega um por vez.
# print(texto.__next__())# função next ele entrega um por vez.
# print(texto.__next__())# função next ele entrega um por vez.
# print(texto.__next__())# função next ele entrega um por vez.
# print(texto.__next__())# função next ele entrega um por vez.
# print(texto.__next__())# função next ele entrega um por vez.
# print(texto.__next__())# função next ele entrega um por vez.
# print(texto.__next__())# função next ele entrega um por vez.
