import sys
input = sys.stdin.readline

N, M = map(int,input().rstrip().split())

array = []
array2 = []
result = []

for _ in range(N):
    array.append(input().rstrip())
for _ in range(M):
    array2.append(input().rstrip())

def calc(array,array2):
    for i in array:
        for j in array2:
            if i == j:
                result.append(i)
    result.sort()
calc(array,array2)

print(len(result))
for i in result:
    print(i)