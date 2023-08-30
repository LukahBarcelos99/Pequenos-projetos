termo = int(input("Digite o valor do TERMO: "))
razao = int(input("Digite o valor da RAZÃO: "))
c = 0
qtde = 10

while qtde != 0:
    while c < qtde:
        termo +=razao
        c += 1
        print(termo, " ", end='')
    qtde = int(input("Quanto termos você quer mostrar mais?"))
    c = 0
print("Com o termo sendo {}, encerramos o programa por aqui!".format(termo))
