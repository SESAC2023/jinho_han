import sys
import math
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))
"""
arr = [
  ("홍길동", 75),
  ("이순신", 95),
  ("김삿갓", 35)
]

# 점수를 기준으로 오름차순 정렬
def compare(x):
    return x[1]

arr.sort(key=compare)
"""

arr = []
n = int(input())


# 점수를 기준으로 오름차순 정렬
def compare(data):
    # <정렬 기준 명시하기>
    # 두 번째 원소를 기준으로 오름차순 정렬
    # 두 번째 원소가 같다면, 첫 번째 원소를 기준으로 오름차순 정렬
    return (data[1], data[0])


for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort(key=compare)

for data in arr:
    print(data[0], data[1])
