import sys
import math
input = sys.stdin.readline

N = int(input())
M = list(map(int,input().split()))
B, C = map(int,input().split())
count = 0
for i in range(N):
    M[i] -= B
    if M[i] > 0:
        count +=  math.ceil(M[i] / C)

print(count+N)