
num_um = int(input('primeiro numero: '))
num_dois = int(input('segundo numero: '))


if num_um > num_dois:
    print("O número {} é maior que o número {}".format(num_um, num_dois))

elif num_um < num_dois:
    print("O número {} é maior que o número {}".format(num_dois, num_um))

else:
    print("numero {} e {} são iguais.".format(num_um, num_dois))