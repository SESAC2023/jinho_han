import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

answer = [0]*N
for iter in range(M):
    i, j, k = map(int, sys.stdin.readline().rstrip().split())
    for start in range(i, j+1):
        answer[start-1] = k

for z in answer:
    print(z, end=' ')
