count = 0 
def contar_chamadas():
    global count 
    count = count + 1

n = int(input())
for i in range(1,n+1):
    contar_chamadas()
    print(count)
