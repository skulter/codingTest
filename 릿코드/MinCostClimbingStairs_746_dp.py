cost = [10,15,20]
# cost = [1,100,1,1,1,100,1,1,100,1]

dp = [0] * int(len(cost) + 1)
dp[0] = cost[0]
dp[1] = cost[1]

for x in range(2, len(cost)+1):
    dp[x] = min(dp[x-1] + cost[x-3] ,dp[x-2] + cost[x-3])
print(dp)



