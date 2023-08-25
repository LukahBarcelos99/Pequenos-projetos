sexo = (input("Informe o seu sexo: ")).strip().upper()[0]

while sexo != 'F' and sexo != 'M':
   sexo = (input("Erro! Digite o seu sexo: ")).strip().upper()[0]
print("Você é do sexo {}".format(sexo))