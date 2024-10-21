class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome           # Atributo que armazena o nome do produto
        self.preco = preco         # Atributo que armazena o preço do produto
        self.quantidade = quantidade  # Atributo que armazena a quantidade disponível

    def aplicar_desconto(self, percentual):  # Método para aplicar desconto
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto
        print(f"O novo preço de {self.nome} após {percentual}% de desconto é R$ {self.preco:.2f}.")

# Criando um objeto da classe Produto
produto1 = Produto("Camiseta", 50.00, 10)
print(produto1.nome)  # Saída: Camiseta
print(produto1.preco)  # Saída: 50.00
print(produto1.quantidade)
produto1.aplicar_desconto(10)  # Saída: O novo preço de Camiseta após 10% de desconto é R$ 45.00.