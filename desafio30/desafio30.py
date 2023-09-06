print("==="*15)
print("COMPRA E VENDA DE LIXOS DO LUCAS")
print("==="*15)
produto = str(input("Digite o nome do produto: "))
preco = float(input("Digite o valor do produto: "))
print("---"*15)
precoBarato = preco
nomePrecoBarato = produto
soma = 0
cont = 0

while True:
    soma += preco
    if preco >= 1000:
         cont += 1
    if precoBarato > preco:
         precoBarato = preco
         nomePrecoBarato = produto
    restart = ' '
    while restart not in "SN":
        restart = str(input("Deseja continuar comprando? ")).strip().upper()[0]
    if restart == "N":
            print("-=="*20)
            break
    produto = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o valor do produto: "))
    print("---"*15)
    
            
print(f"""O total gasto na sua compra foi: R${soma:.2f}.
Em sua compra, existe(em) {cont} produto(s) acima de R$ 1000.00.
O produto mais barato é o {nomePrecoBarato}, custando apenas R${precoBarato:.2f}.
""")