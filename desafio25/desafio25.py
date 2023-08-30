media = 0
num = int(input("Digite um número: "))
autorizacao = False
maior = num
menor = num
cont = 0

while autorizacao != True:
    media += num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    autorizacao = str(input("Você deseja digitar outro número?: ").lower())
    if autorizacao == "sim" or autorizacao == "s":
        num = int(input("Digite outro número: "))
        autorizacao = False
    else:
        autorizacao = True
    cont += 1
media = media / cont
print("A quantidade de números informado é: {}, Média: {}, Menor número: {}, Maior número: {}".format(cont, media, menor, maior))