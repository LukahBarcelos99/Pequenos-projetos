
numUsuario = int(input("Digite um número para saber o fatorial dele: "))
count = numUsuario
fat = 1
while count > 0:
    print("{}".format(numUsuario), end='')
    print(" x " if count > 1 else " = ", end='')
    fat = fat * count
    count -= 1
print(fat)