# 파일 만들기
# 글자 인코딩

# file = open('C:/DEV/Temp/Bank/sample03.txt','w', encoding = 'utf-8')   # 파일을 쓰기로 만듦
file = open('./Day05/sample05.txt','w', encoding = 'utf-8')
# file = open('../sample05.txt','w', encoding = 'utf-8')

file.write('안녕하세요\n')
file.write('두번째 파일입니다.\n')
file.write('절대경로에 파일이 생성될겁니다.\n')

file.close()
print('sample01.txt가 생성되었습니다.')

# ASCII -> 한 단어를 표현하는 체계(영어)
# unicode(UTF-8) -> 모든 나라언어를 다 표현 가능

# 파일/폴더 경로
# 절대경로 : 처음부터 모든 경로 작성 (루트 뭐시라 부터
# 상대경로 : 자신과 자신의 부모를 이용해서 가까운 경로로 이동할떄 사용