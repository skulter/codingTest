# 그리디 알고리즘
# N = int(input())
# count = 0

# while N >= 0:
#     if N % 5 == 0:
#         count += N // 5;
#         print(count)
#         break

#     N = N -3
#     count += 1
# else:
#     print(-1)


# DP
N = int(input())
sugar = [-1] * 5001
sugar[3] = sugar[5] = 1
for i in range(6,N+1):
    if i % 5 == 0:
        sugar[i] = sugar[i-5] + 1
    if i % 3 == 0:
        sugar[i] = sugar[i-3] + 1
    if sugar[i-5] != -1 and sugar[i-3] != -1:
        sugar[i] = min(sugar[i-5], sugar[i-3])+1
print(sugar[N])