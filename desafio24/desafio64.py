soma = 0
cont = 0
n = int(input("Digite um número:"))

while n != 999:
    soma += n
    cont += 1
    n = int(input("Digite um número:"))
print("Foram digitados {} números e a soma entre eles foi dê: {}".format(cont, soma))