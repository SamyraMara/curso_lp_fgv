def formatar_pedido(item,quantidade=1,preço_unidade=0):
    preço_total=int(quantidade)*int(preço_unidade)
    print("Pedido: ",quantidade,"X",item," a R$",preço_unidade," cada. Total: $",preço_total)

item = input("Item: ")
quantidade = input("Quantidade: ")
preço_unidade = input("Preço por unidade: ")
formatar_pedido(item,quantidade,preço_unidade)