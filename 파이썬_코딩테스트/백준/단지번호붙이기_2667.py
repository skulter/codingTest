from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

graph = [list(map(int,input().rstrip())) for _ in range(N)]

answerArr = [0] * int(25)

def bfs(x,y):
    global count
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 0:
                continue
            answerArr[count] += 1
            queue.append((nx,ny))
            graph[nx][ny] = 0
    count +=1

count = 1
for i in range(N):
    for j in range(N):
        bfs(i,j)

answerArr = [i for i in answerArr if i > 0]
answerArr = sorted(answerArr)
print(len(answerArr))
for i in answerArr:
    print(i)