# def 함수명(매개변수):
#     실행할 소스코드
#     return 반환값

# 더하기 함수 예시
def add(a, b):
    return a + b


print(add(3, 7))

#############################################################


def add(a, b):
    print("함수의 결과: ", a+b)


add(3, 7)

#############################################################


def add(a, b):
    print("함수의 결과: ", a+b)


add(a=3, b=7)

#############################################################

#global 키워드
# global 키워드로 변수를 지정하면 해당 함수에서는 지역변수를 만들지 않고,
# 함수 바깥에 선언된 변수를 바로 참조하게 된다.

a = 0


def func():
    global a
    a += 1


for i in range(10):
    func()

print(a)


#############################################################

# 파이썬에서 함수는 여러 개의 반환 값을 가질 수 있다.
def operator(a, b):
    add_bar = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_bar, subtract_var, multiply_var, divide_var


a, b, c, d = operator(7, 3)
print(a, b, c, d)
