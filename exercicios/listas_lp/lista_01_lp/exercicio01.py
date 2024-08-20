          
def perimetro_melhor(n):
    
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
        if temp >= total_triangulos:
            total_triangulos = temp
            melhor_p = p
            
        p += 1
    return melhor_p

n = input()
perimetro_melhor(n)