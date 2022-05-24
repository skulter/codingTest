# https://www.acmicpc.net/problem/2630

#input
# 8
# 1 1 0 0 0 0 1 1
# 1 1 0 0 0 0 1 1
# 0 0 0 0 1 1 0 0
# 0 0 0 0 1 1 0 0
# 1 0 0 0 1 1 1 1
# 0 1 0 0 1 1 1 1
# 0 0 1 1 1 1 1 1
# 0 0 1 1 1 1 1 1

#output
# 9
# 7


# N = int(input())
# paper = []
# o=z = 0
## paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 
# for _ in range(N):
#     paper.append(list(map(int,input().split())))

# def check(x,y,n):
#     global o, z
#     color = paper[x][y]
#     for i in range(x,x+n):
#         for j in range(y,y+n):
#             if color != paper[i][j]:
#                 check(x,y,n//2)
#                 check(x,y+n//2,n//2)
#                 check(x+n//2,y,n//2)
#                 check(x+n//2,y+n//2,n//2)
#                 return
#     if color == 0:
#         o += 1
#     else:
#         z += 1
# check(0,0,N)
# print(o)
# print(z)