# Counter

- 파이썬 collections 라이브러리의 Counter는 등장 횟수를 세는 기능을 제공한다.
- 리스트와 같은 반복 가능한(iterable) 객체가 주어졌을 떄 내부의 원소가 몇 번 씩 등장했는지를 알려준다.

```py
from collections import Counter
counter = Counter(['red','blue','red','green','blue','blue'])
print(counter['blue']) # 'blue'가 등장한 횟수 출력 # 3
print(counter['red']) # 'red'가 등장한 횟수 출력 # 2
print(dict(counter)) # 사전 자료형으로 변환 {'red':2, 'blue':3, 'green': 1}
```
