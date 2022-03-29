N, M = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)






# array.sort(reverse=True)

# def Dduk_slice(array, result, target):
#     count = 0

#     for i in range(N):
#         if array[i] - result > 0:
#             count += array[i] - result
#     if count >= target:
#         return result
#     return Dduk_slice(array, result-1, target)


# print(Dduk_slice(array, array[0]-1, M))
