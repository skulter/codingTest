n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
def check(x, y, N):
    type = graph[x][y]
    size = N // 2
    for i in range(x, x+N):
        for j in range(y, y+N):
            if type != graph[i][j]:
                print('(',end='')
                check(x, y, size)
                check(x, y+size, size)
                check(x+size, y, size)
                check(x+size, y+size, size)
                print(')', end='')
                return
    print(type,end='')
    return


check(0, 0, n)
k