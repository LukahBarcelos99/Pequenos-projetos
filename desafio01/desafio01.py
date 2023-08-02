simular_novamente = 0

while simular_novamente != 'Não':
    #Dados do cliente
    valor_casa = float(input('Qual o valor da casa financiada? '))
    salario_comprador = float(input('Qual é o valor de sua renda? '))
    anos_pagamento = int(input('Em quanto tempo você pretente pagar a casa? '))

    #Espaço ente linhas
    print('')
    #Calculo da prestação mensal e porcentagem necessária para aprovação do financiamento
    valor_anual = valor_casa / anos_pagamento
    valor_mensal = valor_anual / 12
    porcentagem = salario_comprador * 0.3

    if valor_mensal < porcentagem:
        print("Seu financiamento será aprovado!" + 
            "\n A parcela simulada está por: R${:.2f} ".format(valor_mensal))
    elif valor_mensal >= porcentagem:
        print("Infelizmente seu financiamento não será aprovado!" +
            "\n O valor da sua parcela ficou acima de '30%' de seu salário." +
            "\n A parcela simulada está por: R${:.2f} ".format(valor_mensal))
    print('_____________________________________________________________________')
    simular_novamente = input("Deseja simular o financiamento novamente? Digite 'Sim' ou 'não': ")    

print('Obrigado por Simular seu financiamento!')