# import sys
# input = sys.stdin.readline

# N, M = map(int,input().rstrip().split())

# array = []
# array2 = []
# result = []

# for _ in range(N):
#     array.append(input().rstrip())
# for _ in range(M):
#     array2.append(input().rstrip())

# def calc(array,array2):
#     for i in array:
#         for j in array2:
#             if i == j:
#                 result.append(i)
#     result.sort()
# calc(array,array2)

# print(len(result))
# for i in result:
#     print(i)

import sys

input = sys.stdin.readline

N, M = map(int,input().rstrip().split())
array = {}
for _ in range(N+M):
    name = input().rstrip()
    if array.get(name) == None:
        array[name] = 1
    else:
        array[name] += 1

array2 =[]
for key,value in sorted(array.items(), key = lambda x : x[1],reverse=True):
    if value == 2:
        array2.append(key)
        
print(len(array2))
for i in sorted(array2):
    print(i)