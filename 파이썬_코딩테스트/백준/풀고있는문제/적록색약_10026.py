import graphlib
import re


N = int(input())

graph = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

result = 0
result2 = 0


def dfs(x, y, target):
    visited[x][y] = True
    if 0 <= x < N and 0 <= y < N:
        if target == graph[x][y]:
            dfs(x, y+1, graph[x][y])
            dfs(x+1, y, graph[x][y])
            dfs(x-1, y, graph[x][y])
            dfs(x, y-1, graph[x][y])
        else:
             visited[x][y] = False
             return False
    return True


for x in range(N):
    for y in range(N):
        if not visited[x][y]:
            if dfs(x, y, graph[x][y]):
                result += 1

print(result)
