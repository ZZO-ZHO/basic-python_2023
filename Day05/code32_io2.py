# 다중입력

# x,y = input('두 단어를 입력하세요. > ').split()
# print(x)
# print(y)

# 완전 다중입력(개수가 몇개던 노상관)
inputs = list(map(str, input('단어를 입력하세요(개수 노상관) > ').split()))

print(inputs)

inputs = list(map(int, input('정수를 입력하세요(개수 노상관) > ').split()))

print(inputs)
