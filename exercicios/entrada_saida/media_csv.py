import csv

with open('dados.csv', 'r', newline='') as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv)
    soma = 0
    count = 0
    for linha in leitor_csv:
        soma = soma + float(linha['idade'] )
        count = count + 1
        print (soma/count)
        print(linha)
        print(linha['idade'])
    media = soma/count
    print(media)
    
    
    