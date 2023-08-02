#####################################################################################################
                                        DESAFIO DE PROGRAMAÇÃO
                                ------------=----------------------
                                programa de Simulação de empréstimo
#####################################################################################################

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sambendo que ela não pode exceder 30% do salário ou então o emprestimo será negado.

____________________________________________________________________________________________________
5 Q's:

1- Quais são os dados de entrada necessários?
    * Valor da casa
    * Salário do comprador
    * Em quantos anos ele pagará

2- O que devo fazer com estes dados?
    * Calcular o valor da prestação mensal

3- Quais são as restrições deste problema?
    * O valor mensal não pode exceder 30% do salário do comprador.

4- Qual é o resultado esperado?
    * Que o valor da prestação seja APROVADA ou NEGADA

5- Qual é a sequencia de passos a ser feita para chegar ao resultado esperado?
    1 informar valor da casa
    2 Informar salário
    3 Informar o tempo (anual) que pretende pagar a casa.
    4 Cacular as parcelas
        (VAnual = VCasa / AnosPagara
        VMensal = VAnual / 12 meses)
    
    5 Verificar se o valor excede 30% do salário do comprador.
        (porcentagem = salario * 0.3
        Se VMensal <= porcentagem
            Verdade
        CasoContrario
            Mentira)
    6 Retornar resposta ao usuário.
    7 perguntar se deseja realizar outra simulação.
    8 Sim, retorna ao inicio.
    9 Não, finaliza o programa.
    _____________________________________________________________________________________________________