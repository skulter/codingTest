# n = input()
# m = list(input().split())

# dx = [0, -1, 0, 1]
# dy = [1, 0, -1, 0]

# x, y = 1, 1


# def postionValidate(value):
#     if value <= 0:
#         return 1
#     return value


# for i in m:
#     result = 0
#     if i == 'L':
#         y = postionValidate(y + dy[2])
#     elif i == 'R':
#         y = postionValidate(y + dy[0])
#     elif i == 'U':
#         x = postionValidate(x + dx[1])
#     else:
#         x = postionValidate(x + dx[3])

# print(x, y)
#################################################
# 답안 예시
# n = int(input())
n = 5
x, y = 1, 1
# plans = input().split()
plans = 'R R R U D D'.split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if(plan == move_types[i]):
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
