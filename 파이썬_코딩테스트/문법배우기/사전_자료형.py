datas = dict()
datas['사과'] = 'Apple'
datas['바나나'] = 'Banana'
datas['코코넛'] = 'Coconut'

print(datas)
if '사과' in datas:
    print("'사과'를 키로 가지는 데이터가 존재한다")
    
print(datas.keys())
print(datas.values())

for key in datas.keys():
    print(key)
    
for key in datas.keys():
    print(datas[key])
    
b = {
    '홍길동': 97,
    '임꺽정': 98
}

print(list(b.values()))

print(b['홍길동'])
