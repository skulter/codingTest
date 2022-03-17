# if 조건문 1:

# elif 조건문 2:

# else:

# 기타 연산자
# 다수의 데이터를 담는 자료형을 위해 in 연산자와 not in 연산자가 제공됨
# 리스트, 튜플, 문자열, 딕셔너리 모두 사용 가능
# x in 리스트
# x not in 문자열

# 아무것도 처리하고 싶지 않을떄 pass 키워드 사용
# 예시) 디버깅 과정에서 일단 조건문 형태만 만들어놓고 조건무을 처리하는 부분은 비워놓고 싶은 경우

score = 85
if score >= 80:
    pass  # 나중에 작성할 코드
else:
    print('성적이 80점 미만입니다.')

print('프로그램을 종료합니다.')

# 조건부 표현식 ( if~ else 문을 한줄에 작성 가능)
score = 85
result = "Success" if score >= 80 else 'Fail' # 80점 이상이면 Success 미만이면 Fail
print(result)