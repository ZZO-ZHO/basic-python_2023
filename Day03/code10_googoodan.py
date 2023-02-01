# 구구단

for i in range(2,10):
    print('------------- ',i,' 단 -------------')
    for j in range(1,11):
        if j % 2 == 1:
            print(f'{i} x {j:>2} = {i*j:>2}',end='\t|  ')
        else:
            print(f'{i} x {j:>2} = {i*j:>2}')

    print()


# 구구단 한줄 출력
for i in range(2,10):
    print(i,'단',end=' | ')
    for j in range(1,11):
            print(f'{i} x {j} = {i*j:>2}',end='\t')

    print()