Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros


5 Q's:

1- Quais são os dados de entrada necessários?
    o valor a se pagar.
2- O que devo fazer com estes dados?
    Devo calcular o valor a ser pago levando em conta a forma de pagamento do cliente.
3- Quais são as restrições deste problema?
    
4- Qual é o resultado esperado?
    Que seja calculado o valor a se pagar à vista, cartão de débito, cartão de crédito 2x ou 3x mais no cartão de crédito, com os devidos descontos ou juros.

5- Qual é a sequencia de passos a ser feita para chegar ao resultado esperado?
    1 - saber o valor do produto comprado.
    2 - Escolher qual a forma de pagamento
        – à vista dinheiro/cheque: 10% de desconto
            valor_final = valor_produto - (valor_produto * 10 / 100)
        – à vista no cartão: 5% de desconto
            valor_final = valor_produto - (valor_produto *5 /100)
        – em até 2x no cartão: preço formal 
        – 3x ou mais no cartão: 20% de juros
        - Quantas parcelas?
            valor_final = valor_produto + (valor_produto * 20 / 100)
            valor_final = valor_final / parcelas
    3 - Dependendo da forma escolhida, realizar o calculo do pagamento
    4 - Mostrar na tela para o usuário qual o resultado.
    ____________________________________________________________________________