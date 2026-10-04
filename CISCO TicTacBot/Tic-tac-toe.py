from random import randint
from time import sleep

count_td = 0

#inicialização do programa
"""for a in range(101):
    print(f'\rCarregando {a}%', flush=True, end="")
    sleep(0.05)"""

print('\n')
print('¬'*100)
print(f'{" TIC - TAC - TOE ":|^100}')
print('¬'*100)
print('\n')

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
]

#Função que cria o robô
def auto():
    robo = randint(1, 9)
    return robo

while True:

    #Robô começa escolhendo
    robo = auto()
    for linha in range(3):
        for coluna in range(3):
            valor2 = matriz[linha][coluna]
            if robo == valor2:
                matriz[linha][coluna] = 'O'
            else:
                pass

    #mostra os mostra os primeiros dados e a escolha do robô
    for linha in matriz:
        for coluna in linha:
            print(f"[{coluna:^10}]", end="")
        print( )

    #Vez do jogador escolher
    choose = int(input('Choose a number: '))

    #verifica se o número escolhido do jogador ou do robô está dentro da matriz
    for linha in range(3):
        for coluna in range(3):
            valor = matriz[linha][coluna]
            if choose == valor:
                matriz[linha][coluna] = 'X'
            else:
                pass
    
    #mostra os dados depois de escolhido
    for linha in matriz:
        for coluna in linha:
            print(f"[{coluna:^10}]", end="")
        print( )
    print('\n')

    #conta se ainda existe números para jogar
    for linha in matriz:
        for coluna in linha:
            if type(coluna) != int:
                count_td += 1

    if count_td == 9:
        break
    else:
        count_td = 0

    #verifica se o robô ou o jogador formou uma linha de três símbolos iguais

    #<--LINHAS-->:

    if matriz[0][0] == matriz[0][1] and matriz[0][0] == matriz[0][2]:
        print('ganhou na linha 1')
        break
    if matriz[1][0] == matriz[1][1] and matriz[1][0] == matriz[1][2]:
        print('ganhou na linha 2')
        break
    if matriz[2][0] == matriz[2][1] and matriz[2][0] == matriz[2][2]:
        print('ganhou na linha 3')
        break

    #<--COLUNAS-->:

    if matriz[0][0] == matriz[1][0] and matriz[0][0] == matriz[2][0]:
        print('ganhou na coluna 1')
        break
    if matriz[0][1] == matriz[1][1] and matriz[0][1] == matriz[2][1]:
        print('ganhou na coluna 2')
        break
    if matriz[0][2] == matriz[1][2] and matriz[0][2] == matriz[2][2]:
        print('ganhou na coluna 3')
        break

     #<--Diagonais-->:

    if matriz[0][0] == matriz[1][1] and matriz[0][0] == matriz[2][2]:
        print('ganhou na Diagonal 1')
        break
    if matriz[2][0] == matriz[1][1] and matriz[2][0] == matriz[0][2]:
        print('ganhou na Diagonal 2')
        break