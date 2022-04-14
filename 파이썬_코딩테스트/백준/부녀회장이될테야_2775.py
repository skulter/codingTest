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
    
# 정답 
# t = int(input())

# for _ in range(t):  
#     floor = int(input())  # 층
#     num = int(input())  # 호
#     f0 = [x for x in range(1, num+1)]  # 0층 리스트
#     for k in range(floor):  # 층 수 만큼 반복
#         for i in range(1, num):  # 1 ~ n-1까지 (인덱스로 사용)
#             f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
#     print(f0[-1])  # 가장 마지막 수 출력