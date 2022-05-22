import math

def isPrime(x):
    if x == 1:
            return False
    for j in range(2,int(math.sqrt(x))+1):
        if x % j == 0:
            return False
    return True

m, n = map(int,input().split())
prime = []
for i in range(m, n+1):
    if isPrime(i):
        prime.append(i)
print('\n'.join(map(str,prime)))