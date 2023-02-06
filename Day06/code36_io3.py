# 콘솔 출력 보충
# 이스케이프 캐릭터(탈출문자)

print('1. Hello,\r\nWorld')
print('2. Hello,\nWorld')       # 권장

print('3. Hello,\n\tWorld')     # t 탭
print('4. Hello,\n\t\bWorld')   # b 백스페이스

print('5. Hello,\n\'World\'')     # ' 홑따옴표

print('6. Hello,"World"')     # " 쌍따옴표
print('7. Hello,\"World\"')     # " 쌍따옴표 -2

print('8. Hello,\\ World')     # \ 표현

print('9. Hello\0')     # 문자열 끝을 알려줌

# 문자열 포맷팅
# %로 포맷코드를 시작
me = '저'
name = '정재영'
age = 25
print('%s는 %s입니다. %d입니다.'% (me, name, age))

print(f'{254.112233:.2f}')  # 최신식 방식
print('%.4f'%(254.112233))  # %A.B%     A = 전체자릿수(작을경우 노상관) | B = 소수점아래 자릿수(반올림)
