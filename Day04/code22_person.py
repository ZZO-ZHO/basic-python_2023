# 클래스 생성

class Person:
    name = '익명'           # 속성변수
    height = ''
    gender = ''
    blood_type = 'A'

    # 1. 생성자 초기화 추가
    # def __init__(self):
    #     self.name = '홍길동'
    #     self.height = '170'
    #     self.gender = 'M'
    #     self.blood_type = 'AB'

    def __init__(self, name, height, gender) -> None:
        self.name = name
        self.height = height
        self.gender = gender

    def walk(self):         # self 꼭 쓰기
        print(f'{self.name}이(가) 걷습니다.')

    def run(self, option):
        if option == 'Fast':
            self.walk()
            print(f'{self.name}이(가) 빨리 달립니다.')
        else:
            print(f'{self.name}이(가) 천천히 달립니다.')

    def stop(self):
        print(f'{self.name}이(가) 멈춥니다.')


# 2. 생성자외 매직메서드(평선) __str__


def __str__(self) -> str:
  return f'출력 : 이름은 {self.name}, 성별은 {self.gender} 입니다.'

'''
jaeyeong = Person()             # 객체생성을 하면 instance(실체)가 만들어짐
jaeyeong.name = '정재영'
jaeyeong.height = '165'
jaeyeong.gender = 'F'
jaeyeong.blood_type = 'RH+ O'

print(f'{jaeyeong.name}의 혈액형은 {jaeyeong.blood_type}입니다.')

jaeyeong.run('Fast')
'''

'''
# 2. 초기화 후 객체생성
hong = Person()
hong.run('slow')
'''


ashely = Person('애슐리',165,'F')
print(ashely.name)
print(ashely.height)
print(ashely.gender)
print(ashely)

