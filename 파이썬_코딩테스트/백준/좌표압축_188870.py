# 5
# 2 4 -10 4 -9
import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int,input().split()))
array2 = sorted(list(set(array)))

dic = {array2[i]:i for i in range(len(array2))}

for i in array:
    print(dic[i], end = ' ')