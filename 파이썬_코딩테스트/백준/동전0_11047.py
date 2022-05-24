n,k = map(int,input().split())

money = [int(input()) for _ in range(n)]

count = 0
for i in sorted(money,reverse=True):
    if k >= i:
        val = (k // i)
        k -= i * val
        count += val
    else:
        continue

print(count)