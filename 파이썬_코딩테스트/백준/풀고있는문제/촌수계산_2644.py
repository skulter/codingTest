from collections import deque
n = int(input())
i, j = map(int,input().split())
k = int(input())
graph = [[] * i for i in range(n)]
q= deque;
visited = [False] * n

for i in range(k):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start,target):





print(graph)
