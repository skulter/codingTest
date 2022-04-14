N, M = map(int, input().split())
card = list(map(int, input().split()))

d = [0] * M

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = card[i] + card[j] + card[k]
            if sum > M:
                continue
            if d[i] < sum:
                d[i] = sum

print(max(d))
