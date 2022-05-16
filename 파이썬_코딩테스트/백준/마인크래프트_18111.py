import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
matrix = []
for i in range(N):
    matrix += list(map(int,input().split()))

Min = min(matrix)
Max = max(matrix)
s, maxheight = 1e9, 0
for k in range(Min, Max+1):
    temps = 0
    tempb = B
    for i in matrix:
        if s < temps:
            break
        if i > k:
            temps += (i - k) * 2
            tempb += i - k
        else:
            temps += k - i
            tempb -= k - i
    if tempb >= 0 and s >= temps :
        s = temps
        maxheight = max(maxheight,k)
print(s, maxheight)

