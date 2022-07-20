import sys
input = sys.stdin.readline


def dfs(x, y, step, total):
    global answer
    if total + max_val*(4-step) <= answer:
        return

    if step == 4:
        answer = max(answer, total)
        return

    for dx, dy in d:
        nx = x + dx  # 새로운 x 좌표
        ny = y + dy  # 새로운 y 좌표
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if step == 2:
                visited[nx][ny] = True  # 탐색기록
                dfs(x, y, step+1, total+board[nx][ny])
                visited[nx][ny] = False  # 탐색기록 제거

            visited[nx][ny] = True
            dfs(nx, ny, step+1, total+board[nx][ny])
            visited[nx][ny] = False


N, M = map(int, input().split())  # 좌표의 행, 열 개수
board = [list(map(int, input().split())) for _ in range(N)]  # 좌표별 값
max_val = max(map(max, board))  # 모든 좌표 중 최댓값
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 좌표 내 상하좌우
visited = [[False] * M for _ in range(N)]  # 탐색여부 확인용
answer = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = True  # 탐색기록
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False  # 탐색기록 제거
print(answer)
