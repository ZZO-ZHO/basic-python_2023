# if문을 배워요
name = '재영'
state = '아픔'

if name == '재영' :
    print('담당의사를 만난다.',end='\n\n')
    if state == '아픔' :
        print('선생님 배가 아파요')
        print('어떻게 아프세요?')
    else:
        print('어디가 아프세요')
        print('안아픈데요')
        print('어라라')

elif name == '다원' :
    print('주사실로 간다',end='\n\n')
    print('따꿈~')
else:
    print('차례를 기다린다.')

