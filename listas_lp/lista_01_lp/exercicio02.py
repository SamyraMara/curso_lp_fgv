import math

def exercicio02(m,n):
    if math.gcd(m,n) != 1:
        print('Os números devem ser primos entre si')
        return None

    matriz = [[0 for _ in range(n)] for _ in range(n)]
    temp = 1
    
    for i in range(n):
        for j in range(n):
            matriz[i][j] = temp
            temp += m
            if temp > n*n:
                temp -= n*n
    print(matriz)





    
    

    