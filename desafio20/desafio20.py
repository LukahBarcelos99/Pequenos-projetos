primeiroValor = float(input("Digite um valor A: "))
segundoValor = float(input("Digite um valor B: "))
selecao = 0
print("Escolha uma opção para fatorar esse valores: ")
while selecao != 5:
    print("""
    [1] - Somar\n
    [2] - Multiplicar\n
    [3] - Maior\n
    [4] - Novos números\n 
    [5] - Sair do programa\n
        """)
    selecao = int(input("Selecione uma opção: "))

    match selecao:
        case 1:
            soma = primeiroValor + segundoValor
            print(soma)
        case 2:
            multi = primeiroValor * segundoValor
            print(multi)
        case 3:
            if primeiroValor > segundoValor:
                print("{} é maior que {}".format(primeiroValor, segundoValor))
            elif segundoValor > primeiroValor:
                print("{} é maior que {}".format(segundoValor, primeiroValor))
            else:
                print("São iguais!")
        case 4:
            primeiroValor = float(input("Digite outro valor A: "))
            segundoValor = float(input("Digite outro valor B: "))
print("Obrigado, por usar nosso aplicativo!")
