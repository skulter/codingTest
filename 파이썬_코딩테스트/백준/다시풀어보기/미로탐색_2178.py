# 4 6
# 101111
# 101010
# 101011
# 111011

# 15
from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]

def bfs(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))
    print(graph[n-1][m-1])
    
bfs(0,0)
    

