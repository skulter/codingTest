N = int(input())


def fivo(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if(dp[x] != 0):
        return dp[x]
    dp[x] = fivo(x-1) + fivo(x-2)
    return dp[x]


dp = [0] * 91

print(fivo(N))
