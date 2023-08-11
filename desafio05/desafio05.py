primeira_nota = float(input("Digite aqui sua primeira nota: "))
segunda_nota = float(input("Digite aqui sua segunda nota: "))

media = (primeira_nota + segunda_nota) / 2

if media < 5:
    print("Você foi REPROVADO!")
if media >= 5 and media <= 6.9:
    print ("Você está de RECUPERAÇÃO!")
if media >= 7:
    print ("Você foi APROVADO!")