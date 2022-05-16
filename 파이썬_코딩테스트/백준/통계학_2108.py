from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    array.append(int(input()))


# 산술평균
print(round(sum(array)/len(array)))

# 중앙값
array.sort()
print(array[len(array)//2])

# 최빈값


def mode(array):
    modeArray = Counter(array).most_common(2)
    # for i in array:
    #     if i in dicArray:
    #         dicArray[i] += 1
    #     else:
    #         dicArray[i] = 1
    # dicArray2 = sorted(dicArray.items(), key=lambda x: x[1], reverse=True)
    if modeArray[0][1] == modeArray[1][1]:
        print(modeArray[1][0])
    else:
        print(modeArray[0][0])

if len(array) > 1:
    mode(array)
else:
    print(array[0])


# 범위
print(max(array) - min(array))
