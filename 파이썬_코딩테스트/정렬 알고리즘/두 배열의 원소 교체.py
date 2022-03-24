# N, K = map(int, input.split())
# array1 = list(map(int, input.split()))
# array2 = list(map(int, input.split()))
# N , K = 5, 3
# # array1 = [1,2,5,4,3]
# # array2 = [5,5,6,6,5]
# # result = 0;


# array1 = sorted(array1)
# array2 = sorted(array2, reverse=True)

# print(array1, array2)

# for i in range(K):
#     array1[i] = array2[i]
# for j in range(N):
#     result += array1[j];
# print(result)


# 답안

N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()  # 배열 A는 오른차순 정렬
b.sort(reverse=True)

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(K):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
