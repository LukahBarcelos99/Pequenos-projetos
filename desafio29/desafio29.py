masc = maiorIdade = menorIdade = 0
maiorIdade = 0
menorIdade = 0
while True:
    idade = int(input("Digite a idade: "))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input("QUal é o sexo [M/F]: ")).strip().upper()[0]
    if idade > 18:
        maiorIdade += 1
    if sexo == "M":
        masc += 1
    elif sexo == "F":
        if idade < 20:
            menorIdade += 1
    print("---"*30)
    restart = str(input("VocÊ deseja cadastrar mais alguém?")).strip().upper()[0]
    if restart == "N":
        break
print("==="*30)
print(f"Existem {maiorIdade} pessoas cadastradas que são maiores de 18 anos.")
print(f"Foram cadastrados {masc} Homens.")
print(f"Existem {menorIdade} mulheres com menos de 20 anos cadastradas.")    