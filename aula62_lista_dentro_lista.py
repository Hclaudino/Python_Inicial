'''
Listas dentro de listas
'''
#Listas dentro delistas acessando por indice e buscando valor
salas = [
    ['Maria','Helene'],
    
    ['José','Marcos'],
    
    #['Almir','Carlos','Eduarda',(0,10,20,30,40)],
]

# print(salas[0][1]) #colocando desse jeito eu acesso ao indice e ao valor da lista refrenciando 02 indices no print
# print(salas[2][2]) #colocando desse jeito eu acesso ao indice e ao valor da lista refrenciando 02 indices no print
# print(salas[2][3][2]) #buscando dentro da tupla utilizando os indices 

for sala in salas: #ele me retorna as salas
    print(f'A Sala é {sala}')
    for aluno in sala:  # ele me retorna alunos      
        print(aluno) #ele me retorna cada aluno dentro de cada salas