import sys
input = sys.stdin.readline


# def binary(target, array, start, end):
#     while start <= end:
#         mid = (start+end) // 2
#         if target[1] < array[mid][1]:
#             end = mid-1
#         if target[1] >= array[mid][1]:
#             if target[0] == array[mid][0]:
#                 return False
#             else:
#                 return True
#     return False

def search(target, array):
    for search in array:
        if target[1] < search[1]:
            return True
        if target[0] == search[0] and target[1] == search[1]:
            return False
        if target[1] >= search[1]:
            return True
      

# docCount : 문서의 개수
# target : 찾을 문서의 위치
# importansaList : 중요도 순서
def solution(docCount, target, importansaList):
    count = 0
    if docCount == 1:
        return 1
    while True:
        if search(target, importansaList[1:docCount]):
            count += 1
            importansaList.append(importansaList[0])
            importansaList.pop(0)
        else:
            return count


N = int(input())
for _ in range(N):
    docCount, target = map(int, input().split())
    importansaList = list(map(int, input().split()))
    tupleList = []
    for i in range(docCount):
        tupleList.append((i, importansaList[i]))
        
    tupleList.sort(reverse=True)
    print(solution(docCount, tupleList.sort(reverse=True)[target], tupleList))
