def calcular_propriedades_retangulo(comprimento, largura):
    area = comprimento*largura
    perimetro = 2*(comprimento+largura)
    return area, perimetro
result = calcular_propriedades_retangulo(4,7)
print(result)