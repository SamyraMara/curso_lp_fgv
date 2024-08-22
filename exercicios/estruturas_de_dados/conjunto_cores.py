#Crie dois conjuntos com cores diferentes.
cores1 = {'amarelo', 'azul', 'rosa', 'marrom'}
cores2 = {'preto', 'cinza', 'verde', 'roxo', 'laranja'}

#Verifique se há alguma cor em comum entre os dois conjuntos.
print(cores1.intersection(cores2))
#Adicione uma cor ao primeiro conjunto.
cores1.add('laranja')
print(cores1)
#Imprima a união dos dois conjuntos.
print(cores1.union(cores2))