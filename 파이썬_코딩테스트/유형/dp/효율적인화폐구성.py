n, m = map(int, input().split())
moneny = [int(input()) for _ in range(n)]
dp = [10001] * (101)
dp[0] = 0 

for i in moneny:
    dp[i] = 1

for i in range(m+1):
    for j in moneny:
        dp[i] = min(dp[i], dp[i-j] + 1)


print(dp[m])
