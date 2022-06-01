n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
nums = []


def check(x, y, N):
    num = matrix[x][y]
    if N == 1:
        nums.append(num)
        return

    for i in range(x, x + N):
        for j in range(y, y + N):
            if num != matrix[i][j]:
                next = N // 3
                check(x, y, next)
                check(x, y + next, next)
                check(x, y + (2*next), next)
                check(x + next, y, next)
                check(x + next, y + next, next)
                check(x + next, y + (2*next), next)
                check(x + (2*next), y, next)
                check(x + (2*next), y + next, next)
                check(x + (2*next), y + (2*next), next)
                return
    nums.append(num)


check(0, 0, n)
print(nums.count(-1))
print(nums.count(0))
print(nums.count(1))
