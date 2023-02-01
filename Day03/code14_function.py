#  함수

'''
 함수만드는법 3가지
1. 파라미터 O 리턴 O
2. 파라미터 O 리턴 X
3. 파라미터 X 리턴 O
4. 파라미터 X 리턴 X
'''

# 함수정의
def add(x,y):
    result = x + y
    return(result)

def sub(x,y):
    result = x - y
    return(result)

def mul(x,y):
    result = x * y
    return(result)

def div(x,y):
    result = x // y
    return(result)

# 함수호출
print(add(1000,10))
print(sub(1000,10))
print(mul(1000,10))
print(div(1000,10))