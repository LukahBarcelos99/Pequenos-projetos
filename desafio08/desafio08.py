from random import randint
from time import sleep

restart = True
itens = ('PEDRA', 'PAPEL', 'TESOURA')

while restart == True:
    print('''Suas opções:
[0] - PEDRA
[1] - PAPEL
[2] - TESOURA''')
    computador = randint(0,2)
    usuario = int(input('FAÇA SUA JOGADA: '))

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')

    print('-=' * 13)
    print('O computador escolheu {}.'.format(itens[computador]))
    print('O usuário escolheu {}.'.format(itens[usuario]))
    print('-=' * 13)

    if computador == 0: #COMPUTADOR jogou PEDRA
        if usuario == 0:
            print('EMPATE!!\n')
        elif usuario == 1:
            print('JOGADOR GANHOU!\n')
        elif usuario == 2:
            print ('COMPUTADOR GANHOU!\n')
    if computador == 1: #COMPUTADOR jogou PAPEL
        if usuario == 0:
            print ('COMPUTADOR GANHOU!\n')
        elif usuario == 1:
            print('EMPATE!!\n')
        elif usuario == 2:
            print('JOGADOR GANHOU!\n')
    if computador == 2: #COMPUTADOR jogou TESOURA
        if usuario == 0:
            print('JOGADOR GANHOU!\n')
        elif usuario == 1:
            print ('COMPUTADOR GANHOU!\n')
        elif usuario == 2:
            print('EMPATE!!\n')

    #REJOGABILIDADE do jogo
    rejogar = input('Deseja jogar novamente? ')
    if rejogar == 'sim':
        restart = True
    elif rejogar == 'nao':
        restart = False
        print('Obrigado por Jogar!\n')