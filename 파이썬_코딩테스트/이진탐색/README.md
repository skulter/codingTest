# 이진 탐색 알고리즘

- 순차 탐색 : 리스트 안에 있는 특정한 **데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인** 하는 방법
- 이진 탐색 : 정렬되어 있는 리스트에서 **탐색 범위를 절반씩 좁혀가며 데이터를 탐색**하는 방법
  - 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정한다.

## 이진 탐색 동작 예씨

- 이미 정렬된 10개의 데이터 중 값이 4인 원소를 찾는 예시를 살펴보자
- 0 2 `4` 6 8 10 12 14 16 18

1. 시작점 : 0, 끝점 : 9, 중간점 : 4 (소수점 이하 제거, 인덱스를 의미한다.)
   - 중간점 4[8]보다 4가 작으니 끝점을 중간점 -1 로 옮긴다
2. 시작점 : 0, 끝점 : 3, 중간점 : 1 (소수점 이하 제거)
   - 0 2 `4` 6
   - 현재 중간점은 1이기 떄문에 찾고자 하는 값을 찾지못하였다.
   - 이번에는 중간점 1[2]보다 찾고자하는 값인 4가 더 크니 중간점을 포함한 왼쪽에 있는 데이터는 볼 필요가 없다.
3. 시작점 : 2, 끝점 : 3, 중간점 : 2 (소수점 이하 제거)
   - `4` 6
   - 이때 중간점 위치에 있는 2[4]는 우리가 찾고자 하는 값이기 때문에 탐색을 마친다.

## 이진 탐색 시간 복잡도

- 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 횟수는 **log<sub>2</sub>N**에 비례한다.
- 예를 들어 초기 데이터 개수가 32개 일 때, 이상적으로 1단계를 거치면 16개가량의 데이터만 남는다.
  - 2단계를 거치면 8개가량의 데이터만 남는다.
  - 3단계를 거치면 4개가량의 데이터만 남는다.
- 다시 말해 이진 탐색은 탐색 범위를 절반씩 줄이며, 시간 복잡도는 **O(logN)**을 보장한다.

## 이진탐색 구현

**이진탐색\_재귀.py**

```py
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


N, target = map(int, input().split())
array = list(map(int, input().split()))
result = binary_search(array, target, 0, N-1)
if result == None:
    print("해당하는 원소가 없습니다.")
else:
    print(result + 1)

```

**이진탐색_반복.py**

```py
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))


def binary_search(array, target, start, end):
    while(start <= end):
        mid = (start + end) // 2
        if(array[mid] == target):
            return mid
        if(array[mid] > target):
            end = mid-1
        else:
            start = mid + 1

    return None


result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)

```

## 파이썬 이진 탐색 라이브러리

- bisect_left(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
- bisect_right(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

**bisect.py**

```py
from bisect import bisect_left, bisect_right
a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

```

## 값이 특정 범위에 속하는 데이터 개수 구하기

**(bisect)특정범위에속하는데이터개수구하기.py**

```py
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수


def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index-left_index


array = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(array, 4, 4))
print(count_by_range(array, -1, 3))

```
### 파라메트릭 서치 (Parametric Search)
- **파라메트릭 서치**란 최적화 문제를 결정 문제("예" 혹은 '아니오')로 바꾸어 해결하는 기법이다.
  - 예시 : 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
- 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 **이진 탐색을 이용하여 해결**할 수 있다.