#  5 6
#  101010
#  111111
#  000001
#  111111
#  111111


def dfs(x, y, count):
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    if x == n-1 and y == m-1:
        result.append(count)
        return True
    if graph[x][y] == 1:
        count += 1

    dfs(x-1, y, count)
    dfs(x+1, y, count)
    dfs(x, y - 1, count)
    dfs(x, y + 1, count)
    return False


n, m = map(int, input().split())
graph = []
result = []

for _ in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(m):
        count = 0
        dfs(i, j, count)

print(min(list(result)))
