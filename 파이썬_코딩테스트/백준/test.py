from collections import deque

n,m,s = map(int,input().split())
visited = [False] * (n+1)
graph = [[] for i in range(n+1)]


for _ in range(m):
    i, j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)
    graph[i] = sorted(graph[i])
    
def bfs(graph,v,visited):
    queue = deque([v])
    visited[v]= True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

bfs(graph,s,visited)

