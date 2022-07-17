from collections import deque
from glob import glob
n = int(input())
i, j = map(int, input().split())
k = int(input())
tree = [[] * i for i in range(n+1)]
q = deque()
visited = [False] * (n + 1)
result = -1

for _ in range(k):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)


def bfs(start, target):
    global result
    q.append((start, 0))

    while q:
        node, cnt = q.popleft()

        if node == target:
            result = cnt

        for i in tree[node]:
            if not visited[i]:
                visited[i] = True
                q.append((i, cnt+1))


bfs(i, j)

print(result)
