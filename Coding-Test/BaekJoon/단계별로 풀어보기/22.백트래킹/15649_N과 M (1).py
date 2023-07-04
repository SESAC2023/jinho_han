"""
<경우의 수>
1) 순열: itertools.permutation()
  - N개의 원소 리스트에서 중복 없이 M개를 골라 만든 수열
  - N개에서 M개를 고르기 (순서가 다르면 다른 경우)
2) 조합: itertools.combination()
  - N개의 원소 리스트에서 중복 없이 M개를 골라 만든 수열
  - 순서가 달라도 원소가 동일하면 같은 경우
3) 중복 순열: itertools.product()
  - N개의 원소 리스트 중에서 중복을 허용해서 M개를 골라 만든 수열
  - N개에서 M개를 고르기 (순서가 다르면 다른 경우)
4) 중복 조합: itertools.combinations_with_replacement()
  - N개의 원소 리스트에서 중복을 허용해서 M개를 골라 만든 수열
  - 순서가 달라도 원소가 동일하면 같은 경우

→ 실전 코딩, 카카오 코테에서는 사용 가능
→ 삼성전자 코테에서는 사용 못 하게 막는 경우가 있다고 함
  - 그래서 짤 수 있어야 함
"""

import sys

sys.setrecursionlimit(int(1e6))

n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]
selected = []  # 현재 경우에서 선택된 원소들
visited = [False] * n  # 각 원소가 선택되었는가

# cnt = 0


# depth: 현재 재귀에서 선택된 원소의 개수
def dfs(depth):
    global cnt
    if depth == m:
        # 실제로 현재 경우에 대하여 처리하는 부분
        for x in selected:
            print(x, end=" ")
        print()
        # cnt += 1
        return
    for i in range(n):
        if visited[i]:
            continue
        # 백트래킹은 3단계로 재귀 호출
        # (1) 원소 넣기
        selected.append(arr[i])
        visited[i] = True
        dfs(depth + 1)  # (2) 재귀 호출
        # (3) 원소 빼기
        selected.pop()
        visited[i] = False


dfs(0)
# print(cnt)
