ano_atual = 2023

acesso = input("Você precisa se alistar? ")

if acesso == "sim":
    ano_nascimento = int(input("Ano de nascimento: "))
    idade = ano_atual - ano_nascimento
    try:
        if idade == 18:
            print("Você está com 18 anos! Esta é a hora exata de se alistar!")

        elif idade > 18:
            restante_de_ano = idade - 18
            print("Você já está com {} e passou {} ano(s) para se alistar! Corra para se regularizar".format(idade, restante_de_ano))

        elif idade < 18:
            restante_de_ano = 18 - idade
            print("Você já está com {} e faltam {} ano(s) para se alistar!".format(idade))
    except:
        print("Erro dentro do Acesso!")

elif acesso == "nao":
    print("Obrigado por acessar!")

else:
    print("Erro! Revise seu codigo")