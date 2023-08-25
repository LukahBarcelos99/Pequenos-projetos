from random import randint

numSecreto = randint(0, 10)
tentativas = 0
jogada = int(input("Adivinhe o número: "))
while jogada != numSecreto:
    if jogada < numSecreto:
        print('Mais... Tente novamente!')
    elif jogada > numSecreto:
        print('Menos... Tente novamente!')
    jogada = int(input("Jogue denovo: "))
    tentativas += 1
print("VOCÊ ACERTOU! O número secreto é: ", numSecreto)
print("Foi necessária(s) {} jogada(s)".format(tentativas))