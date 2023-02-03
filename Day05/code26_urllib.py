# urllib 패키지 불러오기
from urllib.request import Request, urlopen

req = Request('https://www.naver.com')        # 생성자를 사용해서 객체생성
res = urlopen(req)                            # 함수사용
print(res.status)       # 200 = 프로토콜을 잘 수신했다는 신호

