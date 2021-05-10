#!/usr/bin/env python
# coding: utf-8

# ## Seqeuntial Search

# In[3]:


def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1

print('생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요')
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print('앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸입니다.')
array= input().split()

print(sequential_search(n, target, array))


# ## Binary Search

# In[10]:


def binary_search(array, target,start, end):
    if start>end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid]>target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print('그거 없는데요')
else:
    print(result+1)


# ## Binary Search with loop 

# In[14]:


def binary_search(array, target, start, end):
    while start<= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else: 
            start = mid+1
    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print('그거 없는데요')
else:
    print(result+1)


# ## [practice] 부붐찾기

# In[7]:


# 매장에는 N 종류의 부품 
# 고객으로부터 M 종류의 부품 요청

n = int(input())
shop = list(map(int, input().split()))
m = int(input())
demand = list(map(int, input().split()))

for i in range(m):
    if demand[i] not in shop:
        print('no', end=' ')
    else:
        print('yes', end=' ')


# ### solution with binary search

# In[11]:


n = int(input())
shop = list(map(int, input().split()))
shop.sort()  # 이진 탐색을 위한 sorting 

m = int(input())
demand = list(map(int, input().split()))

for i in demand:
    result = binary_search(shop, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else: 
        print('no', end=' ')


# In[16]:


# string are also sortable

a = ['1', '2', '6', '3','4','5']
a.sort()
print(a)

b = ['a','b','d','c','f','e']
b.sort()
print(b)


# In[21]:


# string replace 

a='abcxef'
a.replace('x','d')


# ## [practice] 떡볶이 떡 만들기 

# In[23]:


# 떡 n개, 요청 길이 m 
# 개별 떡 높이 
# 절단기 최댓값 구하기

n,m = map(int, input().split())
height = list(map(int, input().split()))

start = 0
end = max(height)

# binary search 
result = 0
while(start<=end):
    total = 0 
    mid = (start+end)//2
    for x in height:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid-1
    else:
        result = mid  # 여기에 기록 
        start = mid+1 

print(result)

