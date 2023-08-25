soma = 0
cont = 0
for  c in range (1, 7):
    num = int(input("Digite o valor {}: ".format(c)))
    if num % 2 == 0:
        cont = cont + 1
        soma = soma + num
print("O total de números pares são {} e o total da sua soma de pares é: {}".format(cont, soma))
