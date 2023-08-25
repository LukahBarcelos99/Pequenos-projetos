soma_idade = 0
maior = 0
num_mulheres = 0
homem_velho = 0
for p in range (1, 5):
    print("{} pessoa".format(p))
    nome = str(input("Qual o nome da pessoa? "))
    idade = int(input("Qual a idade da pessoa? "))
    sexo = str(input("Qual o sexo da pessoa? [M/F]"))  
    soma_idade = soma_idade + idade
    if sexo == "M":
        if idade > maior:
            maior = idade
            homem_velho = nome

    if idade < 20 and sexo == "F":
        num_mulheres = num_mulheres + 1
media = soma_idade / p
print("A média de idade do grupo é: ", media)
print("Existem {} mulheres com menos de 20 anos.".format(num_mulheres))
print("O Homem mais velho desse grupo é o {} e ele tem {} anos de idade.".format(homem_velho, maior))
