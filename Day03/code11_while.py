# while문

hit = 0     # 변수초기화

while hit < 10000:      # while true:  = 무한반복
    hit += 1
    print(f'나무를 {hit}번 찍었습니다.')
    if hit == 10:
        print('나무가 쓰러졌습니다')
        break
    else:
        print('나무가 아직 넘어가지 않았습니다.',end='\n\n')

print('나무찍기 완료.')