ano_nascimento = int(input("Seu ano de nascimento: "))
ano_atual = 2023

idade = ano_atual - ano_nascimento

if idade < 0:
    print("Não pode ser menor que 0")
elif idade <= 9:
    print("MIRIM")
elif idade > 9 and idade <= 14:
    print("Infantil")
elif idade > 14 and idade <= 19:
    print("JUNIOR")
elif idade > 19 and idade <= 25:
    print("SENIOR")
elif idade > 25: 
    print("MASTER")
else:
    print("Erro! Impossível Calcular")
