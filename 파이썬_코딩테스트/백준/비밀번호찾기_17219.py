import sys
input = sys.stdin.readline

N, M = map(int,input().split())
password = {}

for _ in range(N):
    name, pw = input().split()
    password[name] = pw
for _ in range(M):
    print(password.get(input().rstrip()))
    