
N = int(input())
M = int(input())
S = input()

searchText = 'IOI'
count = 0

for _ in range(1, N):
    searchText += 'OI'
start = S.find(searchText)

for i in range(start, M,2):
    if S.find(searchText, i) >= 0:
        count += 1
        
print(count)
