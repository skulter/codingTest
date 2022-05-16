n,m,b = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(n)]
counts = []
for i in matrix:
    counts.extend(i)
min_v, max_v = min(counts), max(counts)

print(min_v, max_v)

