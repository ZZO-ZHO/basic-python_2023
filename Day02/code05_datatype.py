# 자료형
None    #값이 없는 값

print(None)
print(0 == None)
print('' == None)

# 숫자형
val = 3
print(type(val))

val = 3.14
print(type(val))

val = 'hello'
print(type(val))

val = 0b1010
print(type(val))

val = 12.15646843515646543543321321321
print(type(val))

val = 4_520_000
print(type(val))

val = 3_099.99
print(type(val))

print("-----------------------------------")

# 문자열
val = 'Life is short, You need Python'
print(val)
print(type(val))

print("-----------------------------------")

val = 'Hello\nWorld'
print(val)
val = 'Hello\tWorld'
print(val)
val = 'Hello\t\bWorld'
print(val)

print("-----------------------------------")

val = '''Life is short,
You need Python'''
print(val)
val = 'Hi, I\'m \'JaeYeong\''
print(val)
val = "Hi, I'm 'JaeYeong'"
print(val)

# 불린형 or 불형
참 = True
거짓 = False

print(1 + 1 == 1)
print(1 + 1 == 2)

print(거짓 == True)
print(거짓 == False)

print(거짓 is False)

print(bool(1)) # 1 == True
print(bool(0)) # 0 == False
print(bool(3)) # 1이외 값은 True X

