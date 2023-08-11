valor_produto = float(input("Digite o valor do Produto: "))

forma_de_pagamento = (int(input("""De qual forma você deseja pagar? 
      \n [1] - À vista dinheiro/cheque
      \n [2] - À vista no cartão
      \n [3] - No cartão de Crédito - 2x Sem juros\n """)))

if forma_de_pagamento == 1:
    valor_final = valor_produto - (valor_produto * 10/100)
    print("""Pagando o valor à vista no DINHEIRO ou CHEQUE, você recebe desconto de 10%! De R${:.2f}, você pagará R${:.2f} \n""".format(valor_produto, valor_final))

elif forma_de_pagamento == 2:
    valor_final = valor_produto - (valor_produto * 5/100)
    print("""Pagando o valor à vista no CARTÃO DE DÉBITO, você recebe desconto de 5%! De R${:.2f}, você pagará R${:.2f} \n""".format(valor_produto, valor_final))

elif forma_de_pagamento == 3:    
    parcelas = int(input("Deseja parcelar de quantas vezes? "))

    if parcelas <= 2 and parcelas > 0:
        valor_final = valor_produto / parcelas
        print("""Pagando No CARTÃO DE CRÉDITO! Você parcelou o valor de R${:.2f} em {}X SEM JUROS ! Você pagará R${:.2f} por parcela.\n""".format(valor_produto, parcelas, valor_final))
        
    elif parcelas > 2 and parcelas <= 12:
        valor_final = valor_produto + (valor_produto * 20/100)
        valor_final_parcelado = valor_final / parcelas
        print("""Pagando No CARTÃO DE CRÉDITO! Você parcelou o valor de R${:.2f} em {}X COM JUROS ! Você pagará um total de R${:.2f}. E pagará R${:.2f} por parcelas.\n""".format(valor_produto, parcelas, valor_final, valor_final_parcelado))
        
    else:
        print("ERRO! Número de parcelas inválido!")
