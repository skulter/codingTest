import sys
input = sys.stdin.readline

n = int(input())

array = list(map(int,input().split()))
array2 = set(array)

def binarySearch(target,array,start,end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] >= target:
            end = mid-1
        else :
            start = mid+1

for i in array:
    print(binarySearch(i,sorted(array2),0,len(array2)-1), end=' ')