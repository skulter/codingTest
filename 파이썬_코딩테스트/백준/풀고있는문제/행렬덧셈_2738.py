N, K = map(int, input().split())
array = []
for _ in range(2):
    array.append([list(map(int, input().split())) for _ in range(N)])

answer = [[0] * K for _ in range(N)]
for i in range(N):
    for j in range(K):
        answer[i][j] = array[0][i][j] + array[1][i][j]
        print(answer[i][j], end=' ')
    print()