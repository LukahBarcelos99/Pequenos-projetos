print("==="*10)
print("{:^30}".format("BANCO DO LUCÃO"))
print("==="*10)

valorSacado = int(input("Qual sera o valor sacado? R$"))
total = valorSacado
cedula = 50
totalCedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1    
    else:
        if totalCedula > 0:
            print(f"Total de {totalCedula} cédula de R${cedula}.")
        if cedula == 50:
            cedula = 20
            totalCedula = 0
        elif cedula == 20:
            cedula = 10
            totalCedula = 0
        elif cedula == 10:
            cedula = 1
            totalCedula = 0
        if total == 0:
            break
print("==="*11)
print("{:^30}".format("Volte sempre ao Banco do LUCÃO!"))
print("==="*11)