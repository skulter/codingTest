# https://www.acmicpc.net/problem/14500
# 입력
# 5 5
# 1 2 3 4 5
# 5 4 3 2 1
# 2 3 4 5 6
# 6 5 4 3 2
# 1 2 1 2 1
# 출력
# 19

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

maxValue = 0
result = []


def solution(x, y):
    global visited, maxValue
    maxValue = matrix[x][y]
    curVal = 0
    curMat = (0, 0)
    prevMat = []
    for _ in range(3):
        for prevX, prevY in prevMat:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                    if curVal < matrix[nx][ny]:
                        curVal = matrix[nx][ny]
                        curMat = (nx, ny)
        x = curMat[0]
        y = curMat[1]
        prevMat.append((x,y))
        visited[x][y] = True
        maxValue += curVal
        curVal = 0
    result.append(maxValue)
    visited = [[False] * M for _ in range(N)]

for x in range(N):
    for y in range(M):
        visited[x][y] = True
        solution(x, y)

print(max(result))
