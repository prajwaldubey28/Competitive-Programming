from collections import defaultdict
from collections import deque
graph = defaultdict(list)
v,e = map(int,input().split())
for i in range(e):
    u,v = map(str,input().split())
    graph[u].append(v)
    graph[v].append(u)
print(graph)

# 1] DFS 
def dfs(graph,start,visited,path):
    path.append(start)
    visited[start] = True
    for k in graph[start]:
        if visited[k] == False:
            dfs(graph,k,visited,path)
    return path 

# 2] BFS
def bfs(graph,start,visited,path):
    queue = deque()
    path.append(start)
    queue.append(start)
    visited[start] = True
    while len(queue)!=0:
        tempnode = queue.popleft()
        for i in graph[tempnode]:
            if visited[i]==False:
                queue.append(i)
                path.append(i)
                visited[i] =True
    return path
                
visited = defaultdict(bool)
start = 'A'
path = []
print(dfs(graph,start,visited,path))
print(bfs(graph,start,visited,path))