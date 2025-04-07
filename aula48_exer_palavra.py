"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
""" 
'''
orientações - eu preciso salvar a letra digitada para que quando o laço  denovo ele salve 
- dentro do while fazer a lógica de exibição do **** ou da letra correta.
- para exibir a letra ou ** preciso percorres a palavra secreta inteira.
'''
import os

palavra_Secreta = 'perfume' #criar as variaveis fora do while para não zerar
letras_acertadas = ' ' #pode ser outras varaiveis mais até agora so vimos STRINGS manter vazia
contador = 0

while True:
    # os.system('cls') colocar aqui vai limpar o termina e não vai dar certo
    
    letra_digitada = input('Digite apenas uma letra: ')
    contador +=1    
        
    if len(letra_digitada) > 1: #fazer a contagem de quantas letras o usuario digitou!
        print("Você digitou mais que uma letra! Digite apenas uma letra..")
        continue
    
    if letra_digitada in palavra_Secreta:
        letras_acertadas += letra_digitada #concaltenar a letras corretas na letras digitas, pois quando volta ela se mantem!
    
    palavra_formada = ''
    for letra_secreta in palavra_Secreta: #serve para percorrer letra por letra
        
        if letra_secreta in letras_acertadas: #varaivel letra_secreta da letras acertadas criada e no if do for
            # print(letra_secreta) # para que eu mude a leitura utilizando o for que é a lógica eu utilizo a linha abaixo
            palavra_formada += letra_secreta #faço a calcoternação nos prints
        else: 
            # print("*")  
            palavra_formada += '*' #utilizo dessa forma!
    print('Palavra formada:', palavra_formada) #fora do else
    if palavra_formada == palavra_Secreta:
        os.system('cls') #aqui fica ótimo
        print(f"Você acertou PARABÉNS A palavra secreta é : {palavra_Secreta}")
        print(f'Você precisou de {contador} para acertar a palavra')
        letras_acertadas = ' ' #colocado aqui novamente para zerar a quantidade
        contador = 0        
        
            
            