#!/usr/bin/env python
# coding: utf-8

# # Sorting

# ### 1. 두 배열 원소 교체 

# In[14]:


n,k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


# In[18]:


A.sort()
B.sort(reverse=True)

for i in range(k):
    if A[i] < B[i]:
        A[i],B[i]=B[i],A[i]
    else:
        break
        
print(sum(A))


# ### 2. 성적이 낮은 순서로 학생 출력하기 

# In[22]:


n = int(input())

info = []
for i in range(n):
    input_data = input().split()
    info.append((input_data[0], input_data[1]))
    
info.sort(key =lambda x: x[1])

for student in info:
    print(student[0])


# ### 3. 위에서 아래로

# In[32]:


n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
    
nums.sort(reverse=True)

for i in range(n):
    print(nums[i], end=' ')


# ### 3. [BAEKJOON] 전화번호 목록

# In[ ]:


# time out 

t = int(input())

for i in range(t):
    n = int(input()) 
    nums = []
    for _ in range(n):
        nums.append(str(input()))
    nums.sort()

    const = 'YES'
    for j in range(n-1):
        if nums[j] == nums[j+1][:len(nums[j])]:
            const = 'NO'
            break
    print(const)

               


# In[ ]:


# startswith()

t = int(input())

for i in range(t):
    n = int(input()) 
    nums = []
    for _ in range(n):
        nums.append(str(input().strip()))
    nums.sort()

    const = 'YES'
    for i in range(len(nums)-1):
        for a,b in zip(nums[i], nums[i+1:]):
            if b.startswith(a):
                const = 'NO'
                break
    print(const)

               
               

