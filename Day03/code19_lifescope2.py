# 전역/지역 변수

num = 1

for i in range(1, 11):
    num = i * num
    print(f'{i + 1}번')

    if i % 3 == 0:
        res = '테스트'
        print(res)

print(f'결과 {num}')
print(res)




'''
함수가 없으면 전역 지역변수 노상관

함수를 쓰거나 뭔가를 호출하면
함수는 지역, 나머지는 전역이 됨
'''