import sys
sys.setrecursionlimit(10 ** 4)
T = int(input())

for _ in range(T):
    m, n, k = map(int, input().split())
    matrix = [[0] * m for _ in range(n)]
    for _ in range(k):
        j, i = map(int, input().split())
        matrix[i][j] = 1

    count = 0

    def bfs(matrix, x, y):
        if x >= n or y >= m or x <= -1 or y <= -1:
            return False
        if matrix[x][y] == 1:
            matrix[x][y] = 0
            bfs(matrix, x+1, y)
            bfs(matrix, x, y+1)
            bfs(matrix, x-1, y)
            bfs(matrix, x, y-1)
            return True
        return False

    for i in range(n):
        for j in range(m):
            if bfs(matrix, i, j):
                count += 1
    print(count)
