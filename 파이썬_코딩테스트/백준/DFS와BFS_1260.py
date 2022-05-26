from collections import deque
# n : 정점의 개수
# m : 간선의 개수
# v : 시작 정점의 번호
n, m, v = map(int, input().split())

graph = [[] for i in range(n+1)]
bfsQueue = deque()
dfsVisited = [False] * (n+1)
bfsVisitred = [False] * (n+1)

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)
    graph[i] = sorted(graph[i])

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    bfsQueue.append(v)
    visited[v] = True
    while bfsQueue:
        v = bfsQueue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if visited[i] == False:
                visited[i] = True
                bfsQueue.append(i)


# print(dfsGraph)
dfs(graph, v, dfsVisited)
print()
bfs(graph, v, bfsVisitred)
