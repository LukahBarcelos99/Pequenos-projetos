num = int(input("Digite um número: "))

mult = 0
for c in range(2,num):
    if num % c == 0:
        print('O número {} é multiplo de {}'.format(num, c))
        mult += 1
    
if mult == 0:
    print('É primo!')
else:
    print('Tem', mult, "Multiplos acima de 2 e abaixo de ", num)
