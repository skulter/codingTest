# # 1
# # 13
# # OOIOIOIOIIOII

# # 4
# import sys
# input = sys.stdin.readline

# N = int(input().rstrip())
# M = int(input().rstrip())
# S = input().rstrip()

# count = 0
# searchText = 'IOI'
# for _ in range(1,N):
#     searchText += 'OI'

# for i in range(M):
#     if S[i:i+len(searchText)] == searchText:
#         count+=1
# print(count)

# 1
# 13
# OOIOIOIOIIOII

# 4
import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
S = input().rstrip()

answer = 0
count = 0
i = 0
 
while i < M:
    if S[i:i+3] == 'IOI':
        i+=2
        count +=1
        if count == N:
            answer += 1
            count -= 1
    else:
        i+= 1
        count = 0
            
print(answer)



