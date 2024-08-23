# Crie uma string com uma frase de sua escolha.
frase = 'te amo'

# Imprima o comprimento da string.
print(len(frase))

# Imprima a string em letras maiúsculas.
print(frase.upper())

# Imprima a string em letras minúsculas.
print(frase.lower())

# Conte o número de vezes que a letra 'a' aparece na string.
count = frase.count('a')
print(count)

# Crie duas strings com seu primeiro e último nome.
first_name =  'Samyra'
last_name = 'Silva'

# Concatene as duas strings para formar seu nome completo.
name = first_name + ' '+ last_name
print(name)

# Separe seu nome completo em duas strings contendo apenas seu primeiro e último nome, respectivamente.
primeiro_nome, ultimo_nome = name.split(' ')
print(primeiro_nome)
print(ultimo_nome)

# Junte as duas strings separadas com um espaço entre elas para formar seu nome completo novamente.
name_completo = primeiro_nome + '' + ultimo_nome
print(name_completo)

# Crie uma string com uma frase que contenha a palavra 'Python'.
frase = 'Estou aprendendo Python'

# Substitua 'Python' por 'Java' na string.
frase = frase.replace("Pytho","Java")
print(frase)

# Crie uma variável com seu nome e idade.
sou = 'Samyra'
idade = 18

# Use formatação de string para criar uma frase que inclua seu nome e idade.
frase_formatada = f"Eu sou a {sou} e tenho {idade} anos"
print(frase_formatada)