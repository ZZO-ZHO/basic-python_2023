# 좀 더 복잡한 계산기

def calc(option, *args):        # *args는 여러개의 인수를 받을수있는 동적 뭐시라~
    result = args[0]
    
    if option == 'add':
        for i in args[1:]:
            result += i

    elif option == 'mul':    
        for i in args[1:]:
            result *= i

    elif option == 'sub':    
        for i in args[1:]:
            result -= i

    elif option == 'div':
        for i in args[1:]:
            result /= i

    return result


# print(calc('add',5,7,17))
# print(calc('mul',512,2,2))
# print(calc('sub',10,248,396))
# print(calc('div',100,5))

# 여러값을 리턴할때는 튜플사용
def new_calc(x,y):
    return(x*y, x/y, x+y, x-y)

#받을때는 튜플 생략 가능
res1, res2, res3, res4 = new_calc(5,7)
# print(res1, res2, res3, res4)