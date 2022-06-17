from collections import deque

INF = int(1e6 + 1)
n, k = map(int, input().split())
dist = [0] * INF


def bfs():
    queue = deque([n])
    while queue:
        num = queue.popleft()
        if num == k:
            print(dist[num])
        for i in (num - 1, num + 1, num * 2):
            if i < INF and not dist[i]:
                dist[i] = dist[num] + 1
                queue.append(i)


bfs()
