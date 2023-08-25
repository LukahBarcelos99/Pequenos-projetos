maior = 0
menor = 0
for p in range (1, 6):
    peso = float(input("Digite o peso da {}º pessoa: ".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso de pessoa é {:.1f}KG".format(maior))
print("O menor peso de pessoa é {:.1f}KG".format(menor))
