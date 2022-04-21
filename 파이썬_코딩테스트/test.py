import sys

N = int(input())
array = []

for _ in range(N):
    array.append(int(input()))

array = sorted(array)
for i in range(N):
    print(array[i])
