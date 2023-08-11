
#Dados do usuário
print('BEM VINDO AO CONVERSOR DE BASES NUMÉRICAS!')

selecao = 0

print('')

while selecao != "4":
    numero_usuario = int(input('Insira um número qualquer: '))

    print('Para converter seu número, escolha a tipo de Base que deseja:'+
        '\n [1] - BINÁRIO'+
        '\n [2] - OCTAL'+
        '\n [3] - HEXADECIMAL'+
        '\n [4] - SAIR \n')
    opcao = int(input("Escolha sua opção: "))
                
    #Condição de escolha do usuário.
    if opcao == 1:
        print("O número {} convertido para BINÁRIO é: {}" .format(numero_usuario, bin(numero_usuario)))
        
        print("")
    elif opcao == 2:
        print("O número {} convertido para OCTAL é: " .format(numero_usuario))
        numero_convertido = oct(numero_usuario)
        print(numero_convertido)
        print("")
    elif opcao == 3:
        print("O número {} convertido para HEXADECIMAL é: " .format(numero_usuario))
        numero_convertido = hex(numero_usuario)
        print(numero_convertido)
        print("")
    elif opcao == 4:
        print('Obrigado por usar o Conversor!')
    else:
        print('Ops! Temos um erro. Verifique os itens disponíveis para selecionar.')
    