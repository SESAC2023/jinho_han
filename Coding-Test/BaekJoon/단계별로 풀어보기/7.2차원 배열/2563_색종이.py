'''
# 해당 문제는 중복된 색종이 부분의 넓이를 빼줘야 한다.
1) 이때 0으로 채워진 전체 종이 좌표(100 by 100)에서
2) 검정색 종이 부분을 1로 채우고, 1을 모두 더하면
3) 최종 넓이가 나온다
'''

import sys

N = 100     # 주어진 종이 전체 좌표 범위
arr = []

for _ in range(N):
    arr.append([0] * N)   # 2차원 행렬로 만듦


M = int(input())
for _ in range(M):
    x, y = map(int, sys.stdin.readline().rstrip().split())  # 입력을 받아, 좌표를 받는다.
    for i in range(x, x+10):                                # 주어진 문제에서 검정색 색종이는 길이가 10인 정사각형이므로, 해당 좌표에서 10만큼씩 x좌표
        for j in range(y, y+10):                            # y좌표에서 훑고 지나오면서 1을 삽입
            arr[i][j] = 1

area = 0
for k in range(N):
    for z in range(N):
        if arr[k][z] == 1:    # 전체 색종이에서 1의 갯수를 세면 넓이가 된다.
            area += 1

print(area)
