from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().rstrip())) for _ in range(N)]

answerArr = []


def bfs(x, y):
    global count
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 0:
                continue
            count += 1
            queue.append((nx, ny))
            graph[nx][ny] = 0


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count = 1
            bfs(i, j)
            answerArr.append(count)

answerArr = sorted(answerArr)
print(len(answerArr))
for i in answerArr:
    print(i)
