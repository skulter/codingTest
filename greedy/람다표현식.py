# 람다 표현식을 이용하면 함수를 간단하게 작성 가능
# 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 특징

def add(a, b):
    return a+b


# 일반적인 add() 메서드 사용
print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a+b)(3, 7))


# 람다 표현식 예시: 내장 함수에서 자주 사용 되는 람다 함수
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]


def my_key(x):
    return x[1]


print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))

# 람다 표현식 예씨 : 여러 개의 리스트에 적용
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2) #각 순번에 맞는 원소끼리 더한다.
print(list(result))
