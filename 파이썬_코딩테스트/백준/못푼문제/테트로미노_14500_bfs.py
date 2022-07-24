import sys
input = sys.stdin.readline

def bfs(y, x, step, maxVal):
    global answer
    if maxVal + max_val*(4-step) <= answer:
        return
    
    if step == 4:
        answer = max(maxVal, answer)
        return

    for dx, dy in d:
        nx = x + dx  # 새로운 x 좌표
        ny = y + dy  # 새로운 y 좌표

        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            if step == 2:
                visited[ny][nx] = True
                bfs(y, x, step+1, maxVal + graph[ny][nx])
                visited[ny][nx] = False

            visited[ny][nx] = True
            bfs(ny, nx, step+1, maxVal + graph[ny][nx])
            visited[ny][nx] = False


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 좌표 내 상하좌우
answer = 0
max_val = max(map(max, graph))  # 모든 좌표 중 최댓값

for y in range(N):
    for x in range(M):
        visited[y][x] = True
        bfs(y, x, 1, graph[y][x])
        visited[y][x] = False

print(answer)
