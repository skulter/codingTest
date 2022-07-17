n = int(input())
i, j = map(int, input().split())
k = int(input())
tree = [[] * i for i in range(n+1)]
visited = [False] * (n + 1)
result = -1

for _ in range(k):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)


def dfs(start, target, visited, cnt):
    global result
    visited[start] = True
    if start == target:
        result = cnt
        return

    for i in tree[start]:
        if not visited[i]:
            dfs(i, target, visited, cnt+1)


dfs(i, j, visited, 0)

print(result)


