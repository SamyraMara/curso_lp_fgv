caminho = 'numeros.txt'
try:
    with open(caminho,mode='r',encoding='utf-8') as fp:
        num_reads = 0
        total = 0
        for line in fp:
            try:
                num = float(line)
                total += num
                num_reads += 1
            except ValueError:
                pass
        print(total)
        if num_reads == 0:
            raise RuntimeError("Nenhum número foi lido.")        
        
except FileNotFoundError:
    print(f"Arquivo passado não existe.\nCaminho: {caminho}")