from collections import deque

queue = deque()

def bfs(graph, v, visited):
    queue.append(v)
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
visited[1] = True
bfs(graph, 1, visited)
