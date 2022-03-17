# N M K
# 5 8 3

n, m, k = map(int, "5 8 3".split())
data = list(map(int, "2 4 5 4 6".split()))

result = 0

data.sort()

first = data[n-1]
second = data[n-2]

firstCount = int(m / (k+1)) * k
firstCount += m % (k+1)

result += firstCount * first
result += (m-firstCount) * second

print(result)
