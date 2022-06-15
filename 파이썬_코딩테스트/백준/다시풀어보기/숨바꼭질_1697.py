from collections import deque
n, k = map(int, input().split())

INF = int(1e5 + 1)
dist = [0] * (INF +1)


def bfs(start):
    queue = deque([start])
    dist[start] = 0

    while queue:
        target = queue.popleft()
        if target == k:
            return dist[target]
        for i in (target+1, target-1, target * 2):
            if  0 <= i < INF and not dist[i]:
                dist[i] = dist[target]+1
                queue.append(i)


print(bfs(n))
