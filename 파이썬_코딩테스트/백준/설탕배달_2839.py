# N = int(input())
# count = 0

# while N >= 0:
#     if N % 5 == 0:
#         count += N // 5;
#         print(count)
#         break
    
#     N = N -3
#     count += 1
# else:
#     print(-1)


N = int(input())
dp =[-1] * 5001

for i in range(3,5001):
    if i % 3 == 0:
        dp[i] = i // 3
    if i % 5 == 0:
        dp[i] = i // 5
    if dp[i-3] > 0 and dp[i-5] > 0:
        dp[i] = min(dp[i-3]+1,dp[i-5]+1)
    
print(dp[N])