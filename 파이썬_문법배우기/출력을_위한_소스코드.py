# 출력할 변수들
a = 1
b = 2
print(a, b)
print(7, end=" ")
print(8, end=" ")

# 출력할 변수
answer = str(7)
print("정답은 " + answer + " 입니다.")


# f-string (javascript ``(백틱)같은 것)
# 파이썬 3.6 부터 사용 가능, 문자열 앞에 접두사 'f'를 붙여 사용
# 중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을 수 있다.

answer = 7
print(f'정답은 {answer} 입니다.')
