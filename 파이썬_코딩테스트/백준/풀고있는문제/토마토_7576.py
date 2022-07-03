from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
q = deque([])
graph = []


def flat(lst):
    result = []
    for item in lst:
        if type(item) == list:
            result += flat(item)
        else:
            result += [item]
    return result


for x in range(M):
    temp = list(map(int, input().split()))
    graph.append(temp)
    for y in range(N):
        if graph[x][y] == 1:
            q.append((x, y))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 0:
            q.append((nx, ny))
            graph[nx][ny] += graph[x][y]+1

graph = flat(graph)
if graph.count(0):
    print(-1)
else:
    print(max(graph)-1)
