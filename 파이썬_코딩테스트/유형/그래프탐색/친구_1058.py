n = int(input())

graph = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
answer = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[k][i] == 'Y' or (graph[k][j] =='Y' and graph[i][j] =='Y'):
                visited[k][i] = 1

for i in range(n):
    for j in range(n):
        if i == j : visited[i][j] = 0

for i in visited:
    answer = max(answer,sum(i))
print(answer)