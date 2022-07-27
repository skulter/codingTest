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

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
INF = int(1e6+1)
n, k = map(int,input().split())
dist = [0] * INF

def bfs():
	queue = deque([n])
		while queue:
			time = queue.popleft()
			if time == k:
				print(dist[num])
			for i in (time - 1, time + 1, time * 2):
				if i < INF and not dist[i]:
					dist[i] = dist[num] + 1
					queue.append(i)

bfs()