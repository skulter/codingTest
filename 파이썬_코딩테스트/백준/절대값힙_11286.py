import heapq
N = int(input())

primeArr = []
arr = []
for _ in range(N):
    n = int(input())
    if n != 0 :
        heapq.heappush(primeArr,abs(n))
        heapq.heappush(arr,n)
    elif n == 0 :
        if len(primeArr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr))
            primeArr.pop(0)
