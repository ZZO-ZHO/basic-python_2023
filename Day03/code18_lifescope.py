# 라이프 스코프

a = 1

def vartest(x):
    global a        # 전역에 있는 a를 함수(지역)에서 가져다 쓰겠다
    x = a + x + 1
    return x

a = vartest(a)
print(a)

