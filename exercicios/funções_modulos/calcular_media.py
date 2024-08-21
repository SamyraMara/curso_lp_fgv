def calcular_media1(nome,*args):
    count = 0
    soma_total = 0
    for num in args:
        soma_total += num
        count = count+1
    media_final = (soma_total/count)
    print("Aluno(a) ", nome, " teve média final ", media_final)
calcular_media1("Eliane", 9, 8.9, 10, 9, 9)

print("\n")

def calcular_media2(nome,*args):
    media = sum(args)/len(args)
    print("Aluno(a) ", nome, " teve média final ", media)
calcular_media2("Lucas", 9.8, 9.3, 10, 9.1, 9)

print("\n")

def lista_media(**kwargs):
    for key in kwargs:
        print(f"aluno(a) {key} teve média final {kwargs[key]}")
lista_media(Mariana="7,6", Eliane="10,0", Victor="9,8", Everton="6,0",)
