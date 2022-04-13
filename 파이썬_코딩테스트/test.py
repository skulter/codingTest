N = int(input())


for i in range(N):
    k = int(input())
    n = int(input())
    array = [[0] * 14 for _ in range(k+1)]
    for i in range(14):
        array[0][i] = i+1
    
    for i in range(1,k+1):
        for j in range(n):
            if j == 0:
                array[i][j] = 1
            elif array[i][j] == 0:
                array[i][j] = array[i-1][j] + array[i][j-1]
    print(array[k][n-1])