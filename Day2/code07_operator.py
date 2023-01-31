# 연산자
# 할당연산

val = 1

# equal 연산자 / 비교연산
print(1 == 1)

# 사칙연산
print(1 + 1)
print(1 - 1)
print(10 * 10)
print(1024 / 2)     # 소수나누기 = 소수점X          ㄱ
print(1024 // 2)    # 정수나누기 = 소수점X          - 0으로는 나눌수없음
print(1024 % 2)     # 나머지
print(10 ** 2)      # 10의 2승 = 10^2
print()

# 문자열연산
first = 'Hello'
second = 'World'

print(first + second)
print(first +' '+ second)
print(first, second)
print(first * 3)
print()

# 문자열 길이 len
print(len(first))
print(first[0])
print(first[1])
print(first[2])
print(first[3])
print(first[4])
# print(first[5]) # Index Error

print("----")

print(first[-1])
print(first[-2])
print(first[-3])
print(first[-4])
print(first[-5])

current = '2023-01-31 15:14:02' #현재시간
print('current의 글자수는 ', end='')
print(len(current))
print(current[0:4] + '년 ' + current[5:7] + '월 ' + current[8:10] + '일' + 
      current[11:13] + '시 ' + current[14:16] + '분 ' + current[17:] + '초')
print()

# 리스트 연산
que = [1, 2, 3, 4, 5]
que[0] = 7

print(que)
#-------------------------------    [리스트]는수정가능 (튜플)은 수정 불가능
tup = (1, 2, 3, 4, 5)
# tup[1] = 9

print(tup)
print()

print('append : 마지막 9추가')
que.append(9)       # 맨마지막에 추가
print(que)

print('insert : 3번째 99추가')
que.insert(3, 99)   # 특정인덱스에 추가
print(que)

print('remove : 99제거')
que.remove(99)      # 해당 값 삭제
print(que)
print()

# 문자열 == 문자리스트
title = 'python'
print(title[0])

# title[0] = 'P'        Error : 일반적인 텍스트만 수정가능
print('P' + title[1:])

text = ['p','y','t','h','o','n']
print(text)
text[0] = 'P'
print(text)

# 문자열 포맷팅
print("I'm so happy {0} you, {1}".format(2,'Hey'))

# 최신식 문자열 포맷팅
preword = 3
sayHello = 'Hey'
print(f"I'm so happy {preword} you, {sayHello}")
print()

pi = 3.141592
print(f'pi는 {pi}입니다.')
print(f'pi는 {pi:0.2f}입니다.')    # 소수점2자리 출력
print(f'pi는 {pi:10.3f}입니다.')    # 정수10자리 소수점3자리 출력

full_name = 'Jeong JaeYeong'
age = 25
print(f'제 이름은 {full_name}입니다. 제 나이는 {age}입니다.')

# 문자열을 특정문자로 자르기
val = full_name.split()     # 그냥 자르면 공백기준으로 잘림 그외는 ()안에 기준 입력
print(val)
print(type(val))

print(full_name.replace('Jeong','정'))

# 문자열 공백 없애기
hi = '          Hello !      Bye ~          '
print(hi.lstrip() + '|')
print(hi.rstrip() + '|')
print(hi.strip() + '|')

print(full_name.index('a'))     # 찾는 단어의 자리수 출력
# print(full_name.index('j'))   # 없는 단어는 Error
print()

print(full_name.find('a'))
print(full_name.find('j'))      # 찾는게 없을경우 -1 출력

print(full_name.count('e'))     # 찾는 단어의 개수 출력
print()

# 모든 단어를 소문자/대문자로 변환
print(full_name.upper())
print(full_name.lower())
print()

# 연산자 우선순위
print(3 + 4 * 2)
print((3 + 4) * 2)