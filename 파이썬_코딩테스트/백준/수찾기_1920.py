import sys

def binarySearch(target, array, start, end):
    while(start <= end):
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        if target < array[mid]:
            end = mid - 1
        elif target > array[mid]:
            start = mid + 1
    return 0


N = int(sys.stdin.readline())
findArray = []
array = []
array = sorted(map(int, sys.stdin.readline().split()))
M = int(input())
findArray = map(int, sys.stdin.readline().split())

for i in findArray:
    count = 0
    print(binarySearch(i, array, 0, N-1))


# for i in range(N):
#     count = 0
#     for j in range(M):
#         if(array[j] == findArray[i]):
#             count += 1
#     if count >= 1:
#         print(1)
#     else:
#         print(0)
