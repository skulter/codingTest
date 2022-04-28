from collections import deque

N = int(input())

array = deque()
for i in range(N):
    array.append(i+1)

while len(array) > 1:
  array.popleft()
  array.append(array.popleft())

print(array.pop())


