# from re import S


# N = int(input())
# card = list(map(int, input().split()))
# M = int(input())
# myCard = list(map(int, input().split()))

# answer = []


# def binary_search(target, array, start, end):
#     count = 0
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             count += 1
#         elif array[mid] >= target:
#             end = mid-1
#         elif array[mid] <= target:
#             start = mid+1

#     answer.append(count)


# card = sorted(card)
# for i in myCard:
#     binary_search(i, card, 0, N-1)

# print(answer)

import sys
from bisect import bisect, bisect_left, bisect_right

N = int(input())
card = list(map(int, sys.stdin.readline().split()))
M = int(input())
myCard = list(map(int, sys.stdin.readline().split()))

answer = []


def binary_search(target, array, start, end):
    count = 0
    count = bisect_right(array, target) - bisect_left(array, target)

    answer.append(count)


card = sorted(card)
for i in myCard:
    binary_search(i, card, 0, N-1)

for i in answer:
    print(i, end=' ')
