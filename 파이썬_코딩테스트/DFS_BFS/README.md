# 그래프 탐색 알고리즘 : DFS / BFS

- 탐색(Search)이란 많은 양의 데이터 중에서 **원하는 데이터를 찾는 과정**을 말한다.
- 대표적인 그래프 탐색 알고리즘으로는 DFS와 BFS가 있다.
- **`DFS/BFS는 코딩 테스트에서 매우 자주 등장하는 유형`** 이므로 반드시 숙지해야 한다.

## 스택 자료구조

- 먼저 들어온 데이터가 나중에 나가는 형식(선입 후출)의 자료구조
- **입구와 출구가 동일한 형태** 로 스택을 시각화 할 수 있다.

```py
stack =[]

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제 - 삽입(1) - 삽입(4) - 삭제()

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) #최상단 원소부터 출력 [1, 3, 2, 5]
print(stack) # 최하단 원소부터 출력 [5, 2, 3, 1]

#append와 pop의 시간복잡도는 O(1) (상수시간)
```

## 큐 자료구조

- 먼저 들어온 데이터가 먼저 나가는 형식(선입선출)의 자료구조.
- 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 할 수 있다.

```py
from collections import deque

# 큐 (Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제 - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력 #deque([3, 7, 1, 4])
queue.reverse() #역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 추력 #deque([4, 1, 7, 3])
#append와 popleft의 시간복잡도는 O(1) (상수시간)
```

# 재귀 함수

- 재귀 함수(Recursive Function)란 자기 자신을 다시 호출하는 함수를 의미한다.
- 단순한 형태의 재귀 함수 예제

  - '재귀 함수를 호출한다' 라는 문자열을 무한히 출력한다.
  - 어느 정도 출력하다가 최대 재귀 깊이 초과 메시지가 출력된다

    ```py
    def recursive_function():
        print('재귀 함수를 호출한다.')
        recursive_function()

    recursive_function()
    ```

## 재귀 함수의 종료 조건

- 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 한다.
- 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있다.

  - **종료 조건**을 포함한 재귀 함수 예제

  ```py
   def recursive_function(i):
        # 100번째 호출을 했을 때 종료되도록 종료 조건 명시
        if i == 100:
            return
        print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출한다.')
        recursive_function(i+1)
        print(i, '번째 재귀함수를 종료한다.')

    recursive_function(1)
  ```

## 팩토리얼 구현 예제

- n! = 1 X 2 X 3 X ··· X (n - 1) X n
- ex) 4! = 4 X 3 X 2 X 1 = 24
- 수학적으로 0!과 1!의 값은 1이다.

```py
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n -1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n-1)

# 각각의 방식으로 구현한 n! 출력 (n = 5)
print("반복적으로 구현:", factorial_iterative(5) )
print("재귀적으로 구현:", factorial_recursive(5) )
```

## 유클리드 호제법 (최대 공약수 계산) 예제

- **두 개의 자연수에 대한 최대 공약수**를 구하는 대표적인 알고리즘으로 유클리드 호제법이 있다.
- **유클리드 호제법**
  - 두 자연수 A, B에 대하여 (A> B) A를 B로 나눈 나머지를 R이라고 하자.
  - 이 때 A와 B의 최대 공약수는 B와 R의 최대 공약수와 같다.
- 유클리드 호제법의 아이디어를 그대로 재귀 함수로 작성할 수 있다.
  - **예시** : GCD(192, 162)
  - | 단계 | A   | B   |
    | ---- | --- | --- |
    | 1    | 192 | 162 |
    | 2    | 162 | 30  |
    | 3    | 30  | 12  |
    | 4    | 12  | 6   |

```py
def gcd(i,j):
    if i % j == 0:
        return j
    else:
        return gcd(j, i % j)

print(gcd(192,162))
```

## 재귀 함수 사용시 유의 사항

- 재귀 함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있다.
  - 단, 오히려 다른 사람이 이해하기 어려운 형태의 코드가 될 수도 있으므로 신중하게 사용해야 한다.
- 모든 **재귀 함수는 반복문을 이용하여 동일한 기능을 구현할 수 있다.**
- 재귀 함수가 반복문보다 유리한 경우도 있고 불리한 경우도 있다.
- 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓인다.
  - 그래서 스택을 사용해야 할 때 구현상 **스택 라이브러리 대신에 재귀 함수를 이용**하는 경우가 많다.

# DFS (Depth-First Search)

- DFS는 **깊이 우선 탐색**이라고도 부르며 **그래프에서 깊은 부분을 우선적으로 탐색**하는 알고리즘
- DFS는 **스택 자료구조(혹은 재귀함수)를 이용**하며, 구체적인 동작 과정은 다음과 같다.
  1. 탐색 시작 노드를 스택에 삽입하고 방문 처리 한다.
  2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
  3. 더 이상 2번의 과정을 수행할 수 없을 떄 까지 반복한다.

## DFS 소스코드 예제

```py
# DFS 메서드 정의
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9
# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

```

# BFS (Breadth-First Search)

- BFS는 **너비 우선 탐색**이라고도 부르며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘이다.
- BFS는 **큐 자료구조**를 이용하며, 구체적인 동작 과정은 다음과 같다.
  1. 탐색 시작 노드를 큐에 삽입하고 방문 처리한다.
  2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리 한다.
  3. 더 이상 2번의 과정을 수행할 수 없을 떄까지 반복한다.

## BFS 소스코드 예제

```py
from collections import deque

# BFS 메서드 정의


def BFS(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

BFS(graph, 1, visited)

```
