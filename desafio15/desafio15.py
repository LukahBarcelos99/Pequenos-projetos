from datetime import datetime

atual = datetime.today().year
total_maior = 0
total_menor = 0
for c in range (1,8):
    nasc = int(input("Em que ano a {}º pessoa nasceu? ".format(c)))
    if (atual - nasc) < 18:
        total_maior = total_maior + 1
    else:
        total_menor = total_menor + 1
print("O Total de pessoas maiores de idade são: ",total_maior)
print("O Total de pessoas menores de idade são: ",total_menor)