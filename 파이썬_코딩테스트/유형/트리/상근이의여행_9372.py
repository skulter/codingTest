# 3 3
# 1 2
# 2 3
# 1 3

# 2
from collections import deque
import sys
input = sys.stdin.readline
ts = int(input())


def bfs(graph, v):
    global visitedCount, visited
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        if visited.count(True) == n:
           return
        for i in graph[v]:
            if not visited[i]:
                visitedCount += 1
                visited[i] = True
                queue.append(i)


for _ in range(ts):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    visitedCount = 0
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    bfs(graph, 1)
    print(visitedCount)
