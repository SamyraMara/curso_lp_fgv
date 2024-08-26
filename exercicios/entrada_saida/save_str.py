def save_str(list):
    with open('saida.txt', 'a', encoding='utf-8') as arquivo:
        for string in list:
            arquivo.write(string + '\n')
      

# Exemplo de uso:
a = input('Escreva uma lista (separada por vírgulas): \n').split(',')
save_str(a)

    