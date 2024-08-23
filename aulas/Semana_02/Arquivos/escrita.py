#Escrevendo com 'w':
arquivo = open('saida.txt', 'w', encoding='utf-8')
arquivo.write('Escrevendo em arquivo\n')
arquivo.write('Mais uma linha')


#Escrevendo com 'a':
arquivo = open('saida.txt', 'a', encoding='utf-8')
arquivo.write('\nAdicionando uma linha ao arquivo')

arquivo = open('saida.txt', 'r', encoding='utf-8')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()