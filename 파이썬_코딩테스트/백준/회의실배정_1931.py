# 입력
# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14


# 출력 : 4
import sys
input = sys.stdin.readline
N = int(input())

array = []
for _ in range(N):
    n, m = map(int, input().split())
    array.append((n, m))

array = sorted(array, key=lambda x: x[0])
array = sorted(array, key=lambda x: x[1])

end = array[0][1]
count = 1

for i in range(1, N):
    if array[i][0] >= end:
        count += 1
        end = array[i][1]

print(count)
