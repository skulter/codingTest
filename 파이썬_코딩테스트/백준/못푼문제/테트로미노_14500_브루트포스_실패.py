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
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

maxValue = 0
result = 0
maxResult = 0


def solution(x, y):
    global visited, maxValue, maxResult
    maxValue = matrix[x][y]
    curVal = 0
    curMat = (0, 0)
    prevMat = []
    for j in range(3):
        if j < 2:
            if maxValue + curVal < maxResult:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                        if curVal < matrix[nx][ny]:
                            curVal = matrix[nx][ny]
                            curMat = (nx, ny)
        else:
            for prevX, prevY in prevMat:
                for i in range(4):
                    nx = prevX + dx[i]
                    ny = prevY + dy[i]
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                        if curVal < matrix[nx][ny]:
                            curVal = matrix[nx][ny]
                            curMat = (nx, ny)
        x = curMat[0]
        y = curMat[1]
        prevMat.append((x, y))
        maxValue += curVal
        curVal = 0
        result = maxValue
    maxResult = max(result, maxResult)


for x in range(N):
    for y in range(M):
        visited[x][y] = True
        solution(x, y)
        visited[x][y] = False

print(maxResult)
