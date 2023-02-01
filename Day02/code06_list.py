# 복합형

# 리스트X
a1 = 1
a2 = 2
a3 = 3
a4 = 4
a5 = 5
a6 = 6
a7 = 7
a8 = 8
a9 = 9
a10 = 10

print(a1+a2+a3+a4+a5+a6+a7+a8+a9+a10)

# 리스트O
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr)
sum = 0
for i in arr:
    sum += i

print(sum)

arr1 = [1, 2, 3]
arr2 = [1.1, 2.2, 3.3]
arr3 = ['Hello', 13, 'World', True]

print(arr1)
print(arr2)
print(arr3)
print(type(arr1))

# 빈 리스트
arr4 = [] 
arr5 = list()
print(arr5)

arr6 = [1, 2, 3, 4,[6, 7, 8,[9, 10]]]
print(arr6)

arr7 =  [[1, 2, 3],[4, 5, 6]]
print(arr7)
print()

# 튜플
tuple1 = (1,2,3,4)
print(tuple1)

arr5.append(4)
print(arr5)

# tuple1.append(4) -튜플은 수정안됨
print()

#딕셔너리
spiderman ={'name' : 'Peter Parker',
             'age' : 18,
          'weapon' : 'web Shooter'}

print(spiderman)
print(spiderman['weapon'])
print(type(spiderman))
print()

# 집합
set1=set([1,2,3,4])
print(set1)

set1=set("Hello World")
print(set1)
