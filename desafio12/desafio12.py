numero = int(input("Digite o número para ver sua tabuada: "))

for c in range (1, 11):
    calculo = numero * c
    print ("{} x {} = {}".format(numero, c, calculo))