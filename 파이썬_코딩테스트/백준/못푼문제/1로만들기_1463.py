N = int(input())

count = 0


def toOne(x):
    if x == 1:
        return 0

    answer = 1 + toOne(x-1)

    if x % 3 == 0:
        answer = min(answer, 1 + toOne(x/3))
    if x % 2 ==0:
        answer = min(answer, 1 + toOne(x/2))

    return answer

print(toOne(N))
