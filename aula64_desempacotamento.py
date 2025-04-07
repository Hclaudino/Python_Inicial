'''
Desempacotamento em chamadas 
de métodos e funções
'''

string = 'ABCD'
lista = ['Maria','Joaquim', 1,20,30,40,'Irlene']
tupla = 'Python', 'é', 'Legal'

salas = [
    ['Maria','Helene'],
    
    ['José','Marcos'],
    
    #['Almir','Carlos','Eduarda',(0,10,20,30,40)],
]

# # a,b,c = lista
# # print(a,c)
# a,*_,u = lista
# print(a,u)
# # p,b,c = lista
# # print(a,c)

# for nome in lista:
#     print(nome, end=' ') 

print(*lista) # é a mesma coisa que passar argumentos
print(*string)
print(*tupla)
print(*salas,sep ='\n')
