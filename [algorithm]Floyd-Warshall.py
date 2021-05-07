#!/usr/bin/env python
# coding: utf-8

# ### self-made code for Floyd-Warshall 

# In[6]:


INF = 1e9

n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]
for k  in range(n+1):
    graph[k][k] = 0

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c
    
for k in range(1, n+1):
    for a in range(1,n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            
for i in range(1,n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print('infinity', end=' ')
        else:
            print(graph[i][j], end=' ')
    print()


# ### [M 기업 코딩테스트] 미래도시 

# #### self coding 

# In[28]:


# 지금 1번 회사에 있음 
# 총 n 회사 있음
# K를 거쳐 X로 가는 이동 시간 
# 회사 간 이동 시간은 연결 되어 있으면 1
# 만약 1 -> K -> X 불가능할 경우 -1 출력

INF = int(1e9)

# input
n,m = map(int, input().split())

graph = [[INF]*(n+1) for i in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0 

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1 

X, K= map(int, input().split())        

# the shortest path
for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])
                
if graph[1][K] == INF or graph[K][X] == INF:
    print(-1)
else:
    print(graph[1][K]+graph[K][X])

