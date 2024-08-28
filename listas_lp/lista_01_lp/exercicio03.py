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
