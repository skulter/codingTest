# > 4 5
# >
# > 00110
# >
# > 00011
# >
# > 11111
# >
# > 00000

def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


m, n = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input())))

count = 0
for i in range(m):
    for j in range(n):
        if dfs(i, j) == True:
            count += 1

print(count)
