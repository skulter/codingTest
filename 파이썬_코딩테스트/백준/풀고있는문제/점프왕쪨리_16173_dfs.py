# https://www.acmicpc.net/problem/16173
import sys
n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
result = False

dx = [1, 0]
dy = [0, 1]


def dfs(x, y):
    global result
    next = graph[x][y]
    graph[x][y] = 0
    if x == n-1 and y == n-1:
        result = True
        return

    for i in range(2):
        nx = x + (dx[i]*next)
        ny = y + (dy[i]*next)
        if 0 <= ny < n and 0 <= nx < n and graph[nx][ny] != 0:
            dfs(nx, ny)


dfs(0, 0)

if result:
    print('HaruHaru')
else:
    print('Hing')
