          
def perimetro_melhor(n):
    
    if n != type(int):
        return None
    
    total_triangulos = 0
    melhor_p = 0
    
    p = 1
    while p <= n:
        count = 0
        
        for a in range(1, p):
            for b in range(a, p - a):
                c = p - a - b
                if a**2 + b**2 == c**2:
                    count += 1
        if count > total_triangulos:
            total_triangulos = count
            melhor_p = p

        p += 1
             
    return melhor_p

n = input()
perimetro_melhor(n)