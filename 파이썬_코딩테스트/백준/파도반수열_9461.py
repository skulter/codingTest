import time

n = int(input())

dp=[0] * 101

dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2
start = time.time()
for i in range(6, 101):
    dp[i] = dp[i-1] + (dp[i-2] - dp[i-3]) + (dp[i-3] - dp[i-4])
print("time:", time.time() - start)
for _ in range(n):
    print(dp[int(input())])    

