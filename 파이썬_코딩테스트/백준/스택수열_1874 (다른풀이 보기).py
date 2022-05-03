import sys
input = sys.stdin.readline

n = int(input())

array = []
target = []
answer =[]
isSuccess = True
for _ in range(n):
    target.append(int(input()))
    
count = 0;
for i in target:
    while True:
        if len(array) > 0 and array[-1] > n:
            isSuccess = False
            break
        if len(array) > 0 and i == array[-1] :
            array.pop()
            answer.append('-')
            break;
        else:
            count += 1
            answer.append('+')
            array.append(count)
if isSuccess:
        print("\n".join(answer))
else:
    print('NO')