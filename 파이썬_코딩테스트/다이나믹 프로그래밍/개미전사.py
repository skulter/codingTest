N = int(input())
array = list(map(int, input().split()))

memo = [0] * 100

memo[0] = array[0]
memo[1] = max(memo[0], array[1])
for i in range(2, N):
    memo[i] = max(memo[i-1],memo[i-2] + array[i])

print(memo[N-1])