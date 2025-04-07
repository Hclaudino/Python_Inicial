"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
linhas = 5
colunas = 5

linha = 1 #contador fora pois pertence ao primeiro while

while linha <= linhas:
    coluna =1 # manter dentro desse while para criar o contador pois se não gera erro
    
    while coluna <= colunas:
        print(f'{linha=},{coluna=}')     #mostra o valor colocando = no f strings
        coluna += 1        
    linha += 1    
print("Acabou")