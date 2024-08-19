n = int(input("Digite um número"))
a = 1
b = 1
temp = 0

for i in range(1,n+1):
    a = b
    print(a)
    b = a + temp
    temp = a

