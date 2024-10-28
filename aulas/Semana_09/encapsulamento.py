# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def __str__(self):
#         return f"Pessoa: {self.nome}, Idade: {self.idade}"

# p1 = Pessoa("Ana", 25)
# print(p1)  # Saída: Pessoa: Ana, Idade: 25

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __eq__(self, outra_pessoa):
        return self.nome == outra_pessoa.nome and self.idade == outra_pessoa.idade

p1 = Pessoa("Ana", 25)
p2 = Pessoa("Ana", 25)
print(p1 == p2)  # Saída: False