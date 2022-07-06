import sys
sys.setrecursionlimit(100000)
N = int(input())

graph = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
result = 0
result2 = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def dfs(x, y):
    target = graph[x][y]
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i];
        ny = y + dy[i];
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == target and not visited[nx][ny]:
            dfs(nx,ny)

for x in range(N):
    for y in range(N):
        if not visited[x][y]:
            dfs(x, y)
            result += 1

visited = [[False] * N for _ in range(N)]
for x in range(N):
    for y in range(N):
        if graph[x][y] == 'R':
            graph[x][y] = 'G'

for x in range(N):
    for y in range(N):
        if not visited[x][y]:
            dfs(x, y)
            result2 += 1


print(result, result2)

