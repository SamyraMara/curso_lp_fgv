         
def exercicio01(n):
    
    if not n.isdigit():
        print("Entrada precisa ser um número inteiro")
        return None
    n = int(n)
    
    total_triangulos = 0
    melhor_p = 0
    p = 1
    
    while p <= n:
        temp = 0
        
        for a in range(1, p):
            for b in range(a, p - a):
                c = p - a - b
                if a**2 + b**2 == c**2:
                    temp += 1
        if temp > total_triangulos:
            total_triangulos = temp
            melhor_p = p
            
        p += 1
    return melhor_p

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

def exercio03(r1, r2):
    
    if not isinstance(r1, tuple) or len(r1) != 4:
        print("Erro: O primeiro retângulo está representado incorretamente.")
        return None
    if not isinstance(r2, tuple) or len(r2) != 4:
        print("Erro: O segundo retângulo está representado incorretamente.")
        return None
    
    for vertice in r1 + r2:
        if not isinstance(vertice, tuple) or len(vertice) != 2:
            print("Erro: Retângulo representado incorretamente.")
            return None
    
    lx1, ly1, lx2, ly2 = [], [], [], []
    
    for i in range(4):
        lx1.append(r1[i][0])
        ly1.append(r1[i][1])
        lx2.append(r2[i][0])
        ly2.append(r2[i][1])
        
    x1_min, x1_max = min(lx1), max(lx1)
    y1_min, y1_max = min(ly1), max(ly1)
    
    x2_min, x2_max = min(lx2), max(lx2)
    y2_min, y2_max = min(ly2), max(ly2)
    
    for i in range(4):
        if x1_min <= lx2[i] <= x1_max and y1_min <= ly2[i] <= y1_max:
            return True
    
    for i in range(4):
        if x2_min <= lx1[i] <= x2_max and y2_min <= ly1[i] <= y2_max:
            return True
    
    return False

def exercicio4(**kwargs):
    def colisao(r1, r2):
        if not isinstance(r1, tuple) or len(r1) != 4:
            print("Erro: O primeiro retângulo está representado incorretamente.")
            return None
        if not isinstance(r2, tuple) or len(r2) != 4:
            print("Erro: O segundo retângulo está representado incorretamente.")
            return None

        for vertice in r1 + r2:
            if not isinstance(vertice, tuple) or len(vertice) != 2:
                print("Erro: Retângulo representado incorretamente.")
                return None

        lx1 = [r1[i][0] for i in range(4)]
        ly1 = [r1[i][1] for i in range(4)]
        lx2 = [r2[i][0] for i in range(4)]
        ly2 = [r2[i][1] for i in range(4)]

        x1_min, x1_max = min(lx1), max(lx1)
        y1_min, y1_max = min(ly1), max(ly1)
        x2_min, x2_max = min(lx2), max(lx2)
        y2_min, y2_max = min(ly2), max(ly2)

        for i in range(4):
            if x1_min <= lx2[i] <= x1_max and y1_min <= ly2[i] <= y1_max:
                return True

        for i in range(4):
            if x2_min <= lx1[i] <= x2_max and y2_min <= ly1[i] <= y2_max:
                return True
        
        return False

    nomes = list(kwargs.keys())
    ret = list(kwargs.values())
    pares = []

    for i in range(len(ret)):
        for j in range(i + 1, len(ret)):
            if colisao(ret[i], ret[j]):
                pares.append((nomes[i], nomes[j]))

    return pares