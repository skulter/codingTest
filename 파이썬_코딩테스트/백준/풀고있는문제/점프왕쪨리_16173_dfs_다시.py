n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
answer = False
dx = [1, 0]
dy = [0, 1]


def dfs(x, y):
    global answer
    if x == n-1 and y == n-1:
        answer = True
        return
    
    next = graph[x][y]
    visited[x][y] = True
    for i in range(2):
        nx = x + dx[i]*next
        ny = y + dy[i]*next
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            dfs(nx, ny)


dfs(0, 0)

if answer:
    print('HaruHaru')
else:
    print('Hing')
