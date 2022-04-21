import sys
import math
A, B, V = map(int, sys.stdin.readline().split())

day = (V-B) / (A-B)
print(math.ceil(day))

# day = 1

# d = [0] * V
# d[0] = 0
# while V > 0:
#     day += 1
#     V -= A
#     if(A > V):
#         break
#     V += B


# print(day)
