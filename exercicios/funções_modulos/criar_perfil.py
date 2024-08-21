def criar_perfil(nome, **kwargs):
    perfil = {"nome": nome}
    for chave, valor in kwargs.items():
        perfil[chave] = valor 
    return perfil

perfil_usuario = criar_perfil("Samyra", Idade=18, Cidade="Rio de Janeiro", Estado= "RJ", Nacionalidade="Brasileira")
print(perfil_usuario)