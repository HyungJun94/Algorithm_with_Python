#!/usr/bin/env python
# coding: utf-8

# ## Data structure: stack 

# In[1]:


stack = []
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
stack.pop()  # 후입선출 구조
stack.append(6)
stack.append(7)

print(stack)


# ## Data structure: queue

# In[3]:


from collections import deque

queue = deque()

queue.append(5)
queue.append(4)
queue.popleft()  # 선입선출 구조 
queue.append(3)
queue.append(2)
queue.append(1)
queue.popleft()

print(queue)
queue.reverse()
print(queue)


# ## Recursive function

# In[8]:


# functional loop 

def recursive(n):
    if n==1:
        print('index has reached 1')
    else:
        print('재귀함수 호출')
        n -= 1
        recursive(n)
    
recursive(10)


# In[7]:


## recursive function practice
## fibonacci sequence 

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)

print(fib(3))
print(fib(10))


# ## DFS(Depth-First Search)

# In[10]:


## 깊이 우선 탐색 
 
def dfs(graph, v, visited):
    # current node: visited
    visited[v]=True
    print(v, end=' ')
    # recursively visit current and other nodes
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# data input
graph = [[]]
n = int(input()) # number of nodes
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [False]*(n+1)
dfs(graph, 1, visited)


# ### BFS(Breadth-First Search)

# In[2]:


# 너비 우선 탐색 
# 가까운 노드부터 탐색 

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:   # while queue is not empty
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] =True 


# data input
graph = [[]]
n = int(input()) # number of nodes
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [False]*(n+1)
bfs(graph, 1, visited)


# ### [practice] 음료수 얼려먹기 

# In[6]:


# 총 아이스크림 개수 구하기 
# NxM 크기의 어름틀
# 0: 연결, 1: 칸막이 

N,M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input() ) ) )  # 00011 이렇게 붙어서 들어오는 경우에는 .split() 쓰면 안됨

def dfs(x,y):
    if x<=-1 or x>=N or y<=-1 or y>=M:
        return False
   
    if graph[x][y]==0:
        # 해당 노드 방문 처리
        graph[x][y]=1
        # 재귀적으로 인접 미방문 노드와 그 노드의 인접 미방문 노드도 전부 방문처리 
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        # 이제 인접 전부 1됨 
        return True
    else:
        return False 

count = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            count += 1
print(count)


# ### [practice] 미로 탈출 

# In[3]:


# 현위치 (1,1)
# 출구는 (N,M)
# 탈출위해 움직여야 하는 최소칸 개수 

# data input
N,M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))
    
# direction
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# escape
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x<0 or new_y<0 or new_x>=N or new_y>=M:
                continue
            if graph[new_x][new_y]==1:
                graph[new_x][new_y] = graph[x][y]+1
                queue.append((new_x, new_y))
    return graph[N-1][M-1]

print(bfs(0,0))

