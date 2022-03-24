# 정렬 알고리즘

- 정렬(Sorting)이란 데이터를 특정한 기준에 따라 순서대로 나열하는 것을 말한다.
- 일반적으로 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용된다.
- 7 5 9 0 3 1 6 2 4 8 -> 여거개의 데이터(카드)를 어떻게 **정렬**할 수 있을까?

## 선택 정렬

- 처리되지 않은 데이터 중에서 **가장 작은 데이터를 `선택`해 맨 앞에 있는 데이터와 바꾸는 것을 반복**한다.

**선택정렬.py**

```py
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = i  # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i] # 스와프
print(array)
```

### 선택 정렬의 시간 복잡도

- 선택 정렬은 N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 한다.
- 구현 방식에 따라서 사소한 오차는 있을 수 있지만, 전체 연산 횟수는 다음과 같다.
- N + (N -1) + (N - 2) + .... + 2
- 이는 (N<sup>2</sup> + N - 2) / 2 로 표현할 수 있는데, 빅오 표기법에 따라서 **O(N<sup>2</sup>)** 이라고 작성한다.

## 삽입 정렬

- 처리되지 않은 데이터를 하나씩 골라 **적절한 위치에 삽입**한다.
- 선택 정렬에 비해 구현 난이도가 높은 편이지만, 일반적으로 더 효율적으로 동작한다.
- 첫 번째 데이터 '7'은 그 자체로 정렬이 되어 있다고 판단, 두 번째 데이터인 '5'가 어떤 위치로 들어갈지 판단한다. '7'의 왼쪽으로 들어가거나 오른쪽으로 들어가거나 두 경우만 존재한다.

**삽입정렬.py**

```py
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):  # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j - 1]:  # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j - 1], array[j]
        else:  # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
print(array)
```

### 삽입 정렬의 시간 복잡도

- 삽입 정렬의 시간 복잡도는 **O(N<sup>2</sup>)** 이며, 선택 정렬과 마찬가지로 반복문이 두 번 중첩되어 사용된다.
- 삽입 정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다.
  - 최선의 경우 O(N)의 시간 복잡도를 가진다.
  - 이미 정렬되어 있는 상태에서 다시 삽입 정렬을 수행하면 어떻게 될까?

## 퀵 정렬

- **기준 데이터를 설정**하고 **그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법**이다.
- 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나이다.
- 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘이다.
- 가장 기본적인 퀵 정렬은 **첫 번쨰 데이터를 기준 데이터(Pivot)로 설정**한다.

### 퀵 정렬이 빠른 이유: 직관적인 이해

- 이상적인 경우 분할이 절반씩 일어난다면 전체 연산 횟수로 O(NlogN)을 기대할 수 있다.
  - 너비 X 높이 = N X logN = NlogN
- 퀵 정렬은 평균의 경우**O(NlogN)** 의 시간 복잡도를 가진다.
- 하지만 최악의 경우 **O(n<sup>2</sup>)** 의 시간 복잡도를 가진다.

**퀵정렬.py**

```py
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start  # 피벗은 첫 번째 원소
    left = start + 1
    right = end

    while(left <= right):  # 인덱스
        # 피벗보다 큰 데이터를 찾을 떄까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right):  # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array)-1)
print(array)

```

**파이썬의 장점을 살린 퀵 정렬.py**

```py
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0] # 피벗은 첫번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

```

## 계수정렬

- 특정한 조건이 부합할 때만 사용할 수 있지만 **매우 빠르게 동작하는** 정렬 알고리즘이다.
  - 계수 정렬은 **데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 떄** 사용 가능하다.
- 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의 경우에도 수행시간 O(N+K)를 보장한다.

```py
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array)+1)

for i in range(count):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
```

- 계수 정렬의 시간 복잡도와 공간 복잡도는 모두 **O(N + K)** 이다.
- 계수 정렬은 떄에 따라서 심각한 비효율성을 초래할 수 있다.
  - 데이터가 0과 999,999로 단 2개만 존재하는 경우를 생각해보자.
- **계수 정렬은 동일한 값을 가지는 데이터가 여러 개 등장할 떄** 효과적으로 사용할 수 있다.
- 성적의 경우 100점을 맞은 학생이 여러 명일 수 있기 떄문에 계수 정렬이 효과적이다.

## 정렬 알고리즘 비교하기

- 앞서 다룬 네 가지 정렬 알고리즘을 비교하면 다음과 같다.
- 추가적으로 대부분의 프로그래밍 언어에서 지원하는 **표준 정렬 라이브러리는 최악의 경우에도 O(NlogN)을 보장하도록 설계되어 있다.**

| 정렬 알고리즘 | 평균 시간 복잡도 | 공간 복잡도 | 특징                                                                           |
| ------------- | ---------------- | ----------- | ------------------------------------------------------------------------------ |
| 선택 정렬     | O(N<sup>2</sup>) | O(N)        | 아이디어가 매우 간단하다.                                                      |
| 삽입 정렬     | O(N<sup>2</sup>) | O(N)        | 데이터가 거의 정렬되어 있을 때 가장 빠르다.                                    |
| 퀵 정렬       | O(NlogN)         | O(N)        | 대부분의 경우에 가장 적합, 충분히 빠르다.                                      |
| 계수 정렬     | O(N + K)         | O(N + K)    | 데이터의 크기가 한정되어 있는 경우에만 사용이 가능하지만 매우 빠르게 동작한다. |

## 선택 정렬과 기본 정렬 라이브러리 수행 시간 비교

수행시간비교.py

```py
from random import randint
import time
from tracemalloc import start

# 배열에 10,000개의 정수를 삽입
array = []
for _ in range(10000):
    # 1부터 100 사이의 랜덤한 정수
    array.append(randint(1, 100))

# 선택 정렬 프로그램 성능 측정
    start_time = time.time()
# 선택 정렬 프로그램 소스 코드
for i in range(len(array)):
    min_index = 1  # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[min_index], array[j] = array[j], array[min_index]

# 측정 종료
end_time = time.time()
# 수행 시간 출력
print("선택 정렬 성능 측정", end_time - start_time)

# 배열을 다시 무작위 데이터로 초기화
array = []
for _ in range(10000):
    # 1부터 100 사이의 랜덤한 정수
    array.append(randint(1, 100))

# 기본 정렬 라이브러리 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

# 측정 종료
end_time = time.time()
print("기본 정렬 라이브러리 성능 측정", end_time - start_time)
```
