n, m = map(int, input().split())
dp = [1e9] * 10001
dp[0] = 0
money = []
for _ in range(n):
    money.append(int(input()))

for i in range(1, len(dp)):
    for j in money:
        if dp[i-j] != 1e9:
            dp[i] = min(dp[i], dp[i-j]+1)
if dp[m] == 1e9:
    print(-1)
else:
    print(dp[m])
