#!/usr/bin/env python
# coding: utf-8

# ### [BAEKJOON] 설탕 배달 

# In[54]:


# data input
N = int(input())

# counting
count = 0 

while N >= 0:
    if N%5 == 0:
        count += N//5 
        print(count)
        break
    N -= 3
    count += 1
else: 
    print(-1)


# ### [BAEKJOON] 카드 구매하기 

# In[195]:


# data input
N = int(input())
P = list(map(int, input().split()))

price = [0]*(N+1)

price[1] = P[0]
price[2] = max(price[1]*2, P[1])

for i in range(3,N+1):
    price[i] = P[i-1]
    for j in range(1, i//2+1):
        price[i] = max(price[i], price[j]+price[i-j])

print(price[N])


# ### [BAEKJOON] 피보나치 수 5

# In[203]:


# sequential : error 

N = int(input())

seq = [0] * (N+1)
seq[1] = 1

for i in range(2,N+1):
    seq[i] = seq[i-1] + seq[i-2]

print(seq[N])


# In[ ]:


# function 

N = int(input())

def fib(N):
    if N <= 1:
        return N 
    else:
        return fib(N-1)+fib(N-2)

print(fib(N))

