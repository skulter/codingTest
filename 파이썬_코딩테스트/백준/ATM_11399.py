n = int(input())

wait = list(map(int, input().split()))
dp = [0] * (n+1)
wait = sorted(wait)

for i in range(0, n):
    dp[i] = wait[i] + dp[i-1]
print(sum(dp))
