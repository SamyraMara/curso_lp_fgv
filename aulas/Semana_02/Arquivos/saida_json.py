import json

dados = {'nome': 'Alice', 'idade': 30, 'cidade': 'São Paulo'}

with open('saida.json', 'w') as arquivo_json:
    json.dump(dados, arquivo_json)