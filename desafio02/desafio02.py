
#Dados do usuário
print('BEM VINDO AO CONVERSOR DE BASES NUMÉRICAS!')

selecao = 0

print('')

while selecao != 4:
    numero_usuario = int(input('Insira um número qualquer: '))

    selecao = input('Para converter seu número, escolha a tipo de Base que deseja:'+
        '\n [1] - BINÁRIO'+
        '\n [2] - OCTAL'+
        '\n [3] - HEXADECIMAL'+
        '\n [4] - SAIR \n')

    
    if selecao == 1:
        print("{0:b}".format(numero_usuario))

    elif selecao == "2":
        numero_convertido = numero_usuario
        oct(numero_convertido)
        print('Seu número convertido para OCTAL é: ', numero_convertido)

    elif selecao == "3":
        numero_convertido = numero_usuario
        hex(numero_convertido)
        print('Seu número convertido para HEXADECIMAL é: ', numero_convertido)

    elif selecao == "4":
        print('Obrigado por usar o Conversor!')
    else:
        print('Ops! Temos um erro. Verifique os itens disponíveis para selecionar.')
    