import sys
input = sys.stdin.readline
n, m = map(int,input().split())
numbs = list(map(int,input().split()))
sumArr = [0]
result = 0

for i in range(1,n+1):
    sumArr.append(numbs[i-1]+ sumArr[i-1])
for _ in range(m):
    i, j = map(int,input().split())
    print(sumArr[j]-sumArr[i-1])