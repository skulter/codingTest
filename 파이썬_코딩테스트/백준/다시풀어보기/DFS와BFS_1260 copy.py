from collections import deque


n, m, v = map(int, input().split())

graph = [[] for i in range(n+1)]
dfsVisited = [False] * (n+1)
bfsVisited = [False] * (n+1)
bfsQueue = deque()

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)
    graph[i] = sorted(graph[i])
    graph[j] = sorted(graph[j])


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    visited[v] = True
    bfsQueue.append(v)
    while bfsQueue:
        v = bfsQueue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if visited[i] == False:
                visited[i] = True
                bfsQueue.append(i)

dfs(graph, v, dfsVisited)
print()
bfs(graph, v, bfsVisited)
