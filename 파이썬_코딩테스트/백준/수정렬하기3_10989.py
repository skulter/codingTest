import sys
N = int(sys.stdin.readline())
array = [0] * 10001
for _ in range(1, N+1):
    num = int(sys.stdin.readline())
    array[num] += 1

for i in range(10001):
    for j in range(array[i]):
        print(i)
    