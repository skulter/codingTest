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
    value = []
    for _ in range(3):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                value.append((matrix[nx][ny],nx,ny))
        maxValue += max(value)
        
        value.clear()
    visited = [[False] * M for _ in range(N)]
    
    result.append(maxValue)

for x in range(N):
    for y in range(M):
        visited[x][y] = True
        solution(x, y)

print(max(result))