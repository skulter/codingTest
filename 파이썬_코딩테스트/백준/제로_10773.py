import sys
N = int(sys.stdin.readline())

array = []
zero = []
for _ in range(N):
    array.append(int(sys.stdin.readline()))

for i in range(N):
    if array[i] == 0:
        zero.pop()
    else:
        zero.append(array[i])
sum_list = sum(zero)
print(sum_list)
