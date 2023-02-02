# 모듈사용

import math as m            # 클래스가 아닌 모듈
import code22_person as p   # 우리가 만든 클래스
from code23_car import Car

'''
print(math.pi)
print(math.sin(0))
print(math.cos(0))
print(math.tan(0))
print(math.ceil(3.8))   # 올림
print(math.floor(3.8))  # 내림
print(math.pow(2,10))   # 승수 = print(2 ** 10)
'''
print(m.pi)

# 우리가 만든 모듈사용
me = p.Person('홍길순',155,'F')

print(me)

#
mycar = Car()
print(mycar)