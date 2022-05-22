# 제곱수인지 아닌지 판별 가능한 배열이 (Ture, False)
# 제곱수끼리 모아둔 배열
# N이 제곱수면 1
# 1 ~ N -> i, n - i 제곱수면 2
# 1 ~ N -> 2개 i,j n - i - j 가 제곱수면 3
# 4

import sys
input = sys.stdin.readline
N = int(input().rstrip())

def chk(n, is_sq, sq):
    if is_sq[n]:
        return 1
    m = len(sq)
    for i in range(m):
        if sq[i] > n:
            break
        if is_sq[n-sq[i]]:
            return 2
    for i in range(m):
        if sq[i] > n:
            break
        for j in range(i,m):
            if sq[i]+sq[j] > n:
                break
            if is_sq[n-sq[i]-sq[j]]:
                return 3
    return 4

# 제곱수 array
is_sq = [False] * 50001
sq = []
i = 1

while i**2 <= 50000:
    is_sq[i**2] = True
    sq.append(i**2)
    i += 1
print(chk(N,is_sq,sq))