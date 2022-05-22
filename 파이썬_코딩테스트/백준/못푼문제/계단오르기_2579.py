N = int(input())
dp = [0] * (N+1)

score = []
for i in range(N):
    score.append(int(input()))
dp[1] = score[0]
for i in range(2, N+1):
    dp[i] = max(dp[i-2] + score[i-1], dp[i-3]+score[i-2] + score[i-1])
print(dp[N])
