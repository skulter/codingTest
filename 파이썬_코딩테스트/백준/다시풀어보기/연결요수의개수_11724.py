import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
count = 0


def dfs(graph, visited, x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(graph, visited, i)


for _ in range(m):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, visited, i)
        count += 1
print(count)
