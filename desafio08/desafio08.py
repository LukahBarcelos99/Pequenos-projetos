import random

rejogabilidade = True

while rejogabilidade == True:
    itemJogador = 0
    itemComputador = 0
    print("""VAMOS JOGAR JOKENPO!
      [1] - PEDRA
      [2] - PAPEL
      [3] - TESOURA""")
    
    itemJogador = int(input("Escolha sua opção: "))
    print(itemJogador)
    itemComputador = random.randint(1,3)

    
    if itemJogador == 1 & itemComputador == 3:
        print ("""Você Escolheu: 1 - PEDRA / Computador Escolheu: 3 - TESOURA""")
        print("Jogador Ganhou!\n")
    elif itemJogador == 2 & itemComputador == 1:
        print ("""Você Escolheu: 2 -PAPEL / Computador Escolheu: 1 - PEDRA""")
        print("Jogador Ganhou!\n")
    elif itemJogador == 3 & itemComputador == 2:
        print ("""Você Escolheu: 3 - TESOURA / Computador Escolheu: 2 - PAPEL""")
        print("Jogador Ganhou!\n")
    elif itemJogador == itemComputador:
        print("EMPATE!\n")
    elif itemJogador > 3 or itemJogador < 1:
        print("Erro! Reinicie o game novamente!")
    else:
        print('Computador Ganhou!\n')
        

    
    restart = input("Deseja jogar novamente? ")
    if restart == "Sim":
        rejogabilidade = True
        itemJogador = 0
        itemComputador = 0
    
    elif restart == "Não":
        rejogabilidade = False


