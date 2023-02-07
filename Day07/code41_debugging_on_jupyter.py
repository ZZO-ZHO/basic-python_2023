# %% [markdown]
# # 주피터 노트북 사용법 학습
# 
# ## 마크다운, 파이선 셀 추가 : 단축키
# - 현재 셀 앞에 셀 추가 : a
# - 현재 셀 뒤에 셀 추가 : b
# - 현재 셀을 마크다운으로 변경 : 포커스만 있는 상태 m
# - 현재 셀을 코드 셀로 변경 : y

# %%
# 최초 작성된 Python 셀

# %% [markdown]
# ## 파이선 셀 실행
# - 셀 실행 : Ctrl + Enter
# - 셀 실행 + 셀 이동(생성) : Shift + Enter
# - 셀 실행 + 아래 셀 생성 : Alt + Enter
# - 주석 처리 : Ctrl + /

# %%
print('Hello, Jupyter!!')
# print('Hello, Jupyter!!')

# %% [markdown]
# ## 디버깅
# 

# %%
arr = [1, '2', True, 'Hello', 3.1415926585]

for i in arr:
    print(i)

# %% [markdown]
# # 함수디버깅

# %%
def plus(x,y):
    val = x + y
    return val

print('더하기')
print(plus(10,4))

# %%
def div(x,y):
    val = x / y
    return val
    
print('나누기')
# print(div(10,0))

print(arr)
arr
# %%



