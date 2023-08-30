from random import randint
print("=-"*15)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-"*15)

qtdeVitorias = 0
while True:
    #Declaração de valores do jogar de da máquina
    numMaquina = randint(0, 10)
    num = int(input("Digite um valor: "))
    escolha = " "
    while escolha not in  "PI":
        escolha = str(input("PAR ou ÍMPAR? [P/I]: ")).strip().upper()[0]
    print("---" * 20)
    
    #Verificação se o total é impar ou par.
    print(f"Você jogou {num} e o computador jogou {numMaquina}.")
    soma = num + numMaquina
    if (soma % 2) == 0:
        result = True
    elif (soma % 2) == 1:
        result = False
   
    #Verifica se o jogador ganhou ou não.
    if escolha == "P":
        if result == True:
            print(f"{soma} é PAR!")
            print("Você GANHOU!")
            qtdeVitorias += 1
        elif result == False:
            print(f"{soma} é IMPAR!")
            print("Você PERDEU!")
            print("---" * 20)
            break
    if escolha == "I":
        if result == True:
            print(f"{soma} é PAR!")
            print("Você PERDEU!")
            print("---" * 20)
            break
        elif result == False:
            print(f"{soma} é IMPAR!")
            print("Você GANHOU!")
            qtdeVitorias += 1
    print("Vamos jogar novamente...")
    print("---" * 20)
print(f"GAME OVER! Você venceu a Máquina {qtdeVitorias} consecutivamente.\n")