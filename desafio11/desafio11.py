
resto = 1
acumulador = 0
soma = 0

for c in range (1, 501, 2):
    resto = c % 3
    if  resto == 0:
        acumulador = acumulador + 1
        soma = soma + c
print('''total de itens: {}\n
soma total: {}'''.format(acumulador, soma))