print("-="*17)
print('BEM VINDO AO PROGRAMA DE TABUADA')
print("-="*17)

cont = multi = 0
while True:
    num = int(input("Digite um número: "))
    if num < 0:
        print("~~"*30)
        print("Obrigado por usar nosso sistema de tabuada! Volte sempre")
        print("~~"*30)
        break
    else:
        for cont in range(0, 10):
            cont += 1
            multi = num * cont
            print(f"{num} x {cont} = {multi}")
        print("-"*20)
    