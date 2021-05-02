#!/usr/bin/env python
# coding: utf-8

# # finding out the optimal combination

# ### 1. coin 0 problem 

# In[172]:


N,K = map(int, input().split())


# In[173]:


coins = list(map(int, input().split()))


# In[54]:


import time


# In[174]:


coins


# In[175]:


start = time.time()

count = 0   # num of coins needed
for coin in coins[::-1]:
    if k//coin != 0:
        count += k//coin
        k = k%coin
    else:
        continue 

print(count)

end = time.time()


# In[169]:


print(end-start)


# ### 2. maximum number of meetings

# In[79]:


N = int(input())


# In[124]:


meetings = [[0,0]]*N
temp = list(map(int, input().split()))

for i in range(N):
    meetings[i] = temp[i*2:i*2+2]


# In[178]:


meetings.sort(key= lambda x: [x[1],x[0]])
meetings


# In[179]:


s = time.time()

count=0 # num of possible meetings
end=0 

for meet in meetings:
    start = meet[0]
    if start >= end:
        count += 1
        end = meet[1] 

print(count)


e = time.time()


# In[127]:


print(e-s)


# ### 3. plummer minimun tape problem

# In[1]:


N,L = map(int, input().split())


# In[38]:


locs = list(map(int, input().split()))
locs.sort()


# In[37]:


count = 0 # num tape 

end = 0 
for loc in locs:
    if loc > end:
        end = loc + L - 0.5
        count += 1
    else:
        continue

print(count)

