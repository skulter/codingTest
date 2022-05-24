N = int(input())
square = [list(map(int, input().split())) for N in range(N)]
z = o = 0


def check(x, y, N):
    global z, o
    color = square[x][y]
    for i in range(x, x+N):
        for j in range(y, y + N):
            if color != square[i][j]:
                check(x, y, N//2)
                check(x, y + N // 2, N//2)
                check(x + N // 2, y, N//2)
                check(x + N// 2, y + N // 2, N//2)
                return
    if color == 0:
        z += 1
    else:
        o += 1


check(0, 0, N)
print(z, o)
