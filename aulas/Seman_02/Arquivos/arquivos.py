arquivo = open('dados.txt', 'r', encoding='utf-8')

"""
#Leitura de todo o conteúdo: Usa o método read().
conteudo = arquivo.read()
print(conteudo)
"""

# Leitura linha a linha: Usa um loop para iterar sobre o arquivo. 
for linha in open('dados.txt', 'r', encoding='utf-8'):
    print(linha, end='')
# ou
arquivo = open('dados.txt', 'r', encoding='utf-8')
for linha in arquivo.readlines():
    print(linha, end='')

arquivo.close()