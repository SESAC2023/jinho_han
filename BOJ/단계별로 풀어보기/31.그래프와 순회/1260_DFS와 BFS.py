import sys
from collections import deque

# 재귀 함수 깊이 해제
sys.setrecursionlimit(int(1e6))

input = sys.stdin.readline
N, M, V = map(int, input().rstrip().split())

graph = [[] for i in range(N + 1)]
visited = [False] * (N + 1)

for i in range(M):
    x, y = map(int, input().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N+1):
    graph[i].sort()

'''
graph = [
    [],
    [2,3,4],
    [1,4],
    [1,4],
    [1,2,3],
    []
]
'''


def dfs(x):
    visited[x] = True
    print(x, end=' ')
    for y in graph[x]:
        if not visited[y]:
            dfs(y)

dfs(V)
print()


# BFS 수행
q = deque()
visited = [False] * (N + 1)
visited[V] =  True
q.append(V)

while q:
    x = q.popleft()
    print(x, end=' ')
    for y in graph[x]:
        if not visited[y]:
            visited[y] = True
            q.append(y)
