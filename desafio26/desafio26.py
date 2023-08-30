soma = cont = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    else:
        cont += 1
        soma += n
print(f"Foram digitados {cont} e a soma entre eles é um total de {soma}")