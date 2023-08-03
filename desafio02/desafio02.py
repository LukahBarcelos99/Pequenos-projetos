
#Dados do usuário
print('BEM VINDO AO CONVERSOR DE BASES NUMÉRICAS!')

selecao = 0

print('')

while selecao != "4":
    numero_usuario = int(input('Insira um número qualquer: '))

    selecao = input('Para converter seu número, escolha a tipo de Base que deseja:'+
        '\n [1] - BINÁRIO'+
        '\n [2] - OCTAL'+
        '\n [3] - HEXADECIMAL'+
        '\n [4] - SAIR \n')

    #Condição de escolha do usuário.
    if selecao == "1":
        print("O número {} convertido para BINÁRIO é: " .format(numero_usuario))
        numero_convertido = bin(numero_usuario)
        print(numero_convertido)
        print("")
    elif selecao == "2":
        print("O número {} convertido para OCTAL é: " .format(numero_usuario))
        numero_convertido = oct(numero_usuario)
        print(numero_convertido)
        print("")
    elif selecao == "3":
        print("O número {} convertido para HEXADECIMAL é: " .format(numero_usuario))
        numero_convertido = hex(numero_usuario)
        print(numero_convertido)
        print("")
    elif selecao == "4":
        print('Obrigado por usar o Conversor!')
    else:
        print('Ops! Temos um erro. Verifique os itens disponíveis para selecionar.')
    