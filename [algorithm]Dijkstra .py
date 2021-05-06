#!/usr/bin/env python
# coding: utf-8

# ### 1. Dijkstra

# In[11]:


INF = int(1e9) # 10 억 

# 노드의 개수, 간선의 개수 입력
n,m = map(int, input().split())
# 시작 노드 번호 
start = int(input())
# 연결 정보 
graph = [[] for i in range(n+1)]
# 방문 여부 
visited = [False]*(n+1)
# 초기화 
distance = [INF]*(n+1)

# 간선 정보 
for _ in range(m):
    a,b,c = map(int, input().split())
    # a -> b cost : c
    graph[a].append((b,c))
    
# 방문하지 않은 노드 중 최단거리 노드 
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index 
    
def dijkstra(start):
    # 시작노드 초기화 
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드 제외 n-1 노드에 반복
    for i in range(n-1):
        # 최단 거리 가장 짧은 노드 방분처리 
        now = get_smallest_node()
        visited[now] = True
        # 현재노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 
            if cost < distance[j[0]]:
                distance[j[0]] = cost 
                
# 다익스트라 알고리즘 수행 
dijkstra(start)

# 모든 노드로 가기 위한 최단거리 출력 
for i in range(1, n+1):
    # 도달할 수 없는 경우 INF
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])
    
    
    
    


# ### 2. improved Dijkstra using Heap 

# In[12]:


import heapq
INF = int(1e9) # 10 억 

# 노드의 개수, 간선의 개수 입력
n,m = map(int, input().split())
# 시작 노드 번호 
start = int(input())
# 연결 정보 
graph = [[] for i in range(n+1)]
# 방문 여부 
visited = [False]*(n+1)
# 초기화 
distance = [INF]*(n+1)

# 간선 정보 
for _ in range(m):
    a,b,c = map(int, input().split())
    # a -> b cost : c
    graph[a].append((b,c))
    
# 방문하지 않은 노드 중 최단거리 노드 
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index 
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
# 다익스트라 알고리즘 수행 
dijkstra(start)

# 모든 노드로 가기 위한 최단거리 출력 
for i in range(1, n+1):
    # 도달할 수 없는 경우 INF
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])
    
    
    
    


# In[ ]:




