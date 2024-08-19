"""
n = input("Digite um número")
print(type(n))
n = int(n)
print(type(n))
print(n)

total = 0
for i in range(n):
    total +=1
    print(total)

print("Hello word!")
"""
import sys

n =  sys.argv[1]
n = int(n)

total = 0
for i in range (1, n+1):
    total += i
print(total)
