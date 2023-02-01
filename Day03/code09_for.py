#  for문
arr = [1,2,3,4,5]
sum = 0

for item in arr:
    print(f'{item:2.2f}')       # print(item)
    sum += item

print('합계는 ',sum)


# 리스트 편하게 만드는 방법
vals = [i for i in range(1,11)]
print(vals)

# continue / break      반복문에서만 사용가능
num = 0
for item in vals:
    num += 1
    if num % 2 == 0:
        continue    #이후의 것을 수행하지않고 다시 리턴
        break       #for문 완전 탈출
    else:
        print(num,'번 수는 ',item,'입니다.')

print(range(0,10))