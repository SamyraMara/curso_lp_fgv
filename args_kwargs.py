def exibir_soma(*args):
    total = 0
    for num in args:
        total += num
    print(total)
exibir_soma(1, 2, 3, 4, 5)

def saudação(**kwargs):
    for key in kwargs:
        print(f"{key} diz: {kwargs[key]}")
saudação(Joao="Oi", Maria="Olá", Ana="Oi pessoal!")