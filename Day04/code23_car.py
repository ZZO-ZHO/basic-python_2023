# 자동차 클래스

import code

class Car:                                      # 녹색은 클래스
    __number = '359버 1248'                         

    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number =  number


    def __init__(self, number = '359버 1248') -> None:
        print('__init__')
        self.__number =  number

    '''
    # def __new__(cls):
    #     print('__new__')
    #     return super().__new__(cls)     # 부모클래스(상속)
    '''
    # 부모클래스를 생성자를 생성해서 new를 실행
    def __str__(self) -> str:
        return f'차번호는 {self.__number}'

yourcar = Car()
yourcar.__number = '77거 7777'  # 외부에서는 멤버변수에 접근 불가
print('클래스 내부함수 사용')
yourcar.set_number('77거 7777')
print(yourcar)


mycar = Car()
print(mycar)
print(f'제차는 X4이고 차량번호는 {mycar.get_number()}입니다')


mycar.__number = '111거 1111'
print(mycar.__number)
print(mycar)