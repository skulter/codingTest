from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
answer = False

dx = [1, 0]
dy = [0, 1]
queue = deque()


def bfs(x, y):
    global answer
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        next = graph[x][y]
        visited[x][y] = True
        if x == n-1 and y == n - 1:
            answer = True
            return
        for i in range(2):
            nx = x + (dx[i] * next)
            ny = y + (dy[i] * next)
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                queue.append((nx, ny))


bfs(0, 0)

if answer:
    print('HaruHaru')
else:
    print('Hing')
