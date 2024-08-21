def verificar_par_impar(num):
    if (num % 2) == 0:
        return "Par"
    else:
        return "Ímpar"
num = input()
print(verificar_par_impar(int(input())))
