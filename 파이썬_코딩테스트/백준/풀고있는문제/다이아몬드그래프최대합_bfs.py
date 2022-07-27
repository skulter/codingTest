# input
# 4
# 3
# 5 6
# 7 8 9
# 3 4 7 9
# 5 4 1
# 2 3
# 5

# answer:3 6 9 9 1 3 5 = 36

# ex
# 7
#         1
#        2 3
#       4 5 6
#      7 8 9 10
#   11 12 13 14 15
#  16 17 18 19 20 21
# 21 22 23 24 25 26 27
#  28 29 30 31 32 33
#   34 35 36 37 38
#     39 40 41 42
#      43 44 45
#        46 47
#          48
# input

# 7
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# 21 22 23 24 25 26 27
# 28 29 30 31 32 33
# 34 35 36 37 38
# 39 40 41 42
# 43 44 45
# 46 47
# 48


# answer : 1 3 6 10 15 21 27 33 38 42 45 47 48 =  336

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n*2-1)]
answer = 0


def dfs(level, maxVal, node):
    global answer
    if level == n*2-1:
        answer = max(answer, maxVal)
        return
    for i in graph[level]:
        node = graph[level].index(i)
        left = node
        right = node + 1

        dfs(level+1, maxVal + i, )


dfs(0, 0, 0)

print(answer)
