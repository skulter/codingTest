# N = int(input())
# array = (list(map(int, input().split())))
# count = 0


# def primenumber(x):
#     if x == 1:
#         return False
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True


# for i in array:
#     if primenumber(i) == True:
#         count += 1
# print(count)

import math
def isPrime(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if x == 1:
            return False
        if x % i == 0:
            return False
    return True

N = int(input())
array = (list(map(int, input().split())))
count = 0
for i in array:
    if isPrime(i) == True:
        count +=1
print(count)

# 에라토스테네스의 체
# import math

# def is_prime_num(n):
#     arr = [True] * (n + 1)
#     arr[0] = False
#     arr[1] = False

#     for i in range(2, int(math.sqrt(n)+1)):
#         if arr[i] == True:
#             j = 2

#             while (i * j) <= n:
#                 arr[i*j] = False
#                 j += 1

#     return arr

# arr = is_prime_num(93000)

# for i in range(len(arr)):
#     if arr[i] == True:
#         print(i, end=' ')