import sys
input = sys.stdin.readline
n = int(input())

timer = [300, 60, 10]
count = [0, 0, 0]

for i in range(len(timer)):
    count[i] = n // timer[i]
    n %= timer[i]

if n == 0:
    print(' '.join(map(str, count)))
else:
    print(-1)
