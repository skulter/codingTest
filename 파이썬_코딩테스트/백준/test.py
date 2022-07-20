# 1
# 5 3
# 1 0 0 1 0
# 0 1 0 0 1
# 0 0 0 1 0
# 0 0 0 0 0
# 0 0 1 0 0
import sys
input = sys.stdin.readline
ts = int(input())
for _ in range(ts):
    N, K = map(int, input().split())
    minBoom = 1e9
    graph = [list(map(int, input().split())) for i in range(N)]
    result = []

    for y in range(N-K+1):
        for x in range(N-K+1):
            result.append(sum(sum([row[x:x+K] for row in graph[y:y+K]], [])))
    print(minBoom)
