import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

answer = [i for i in range(1, N+1)]
temp = [i for i in range(1, N+1)]

for iter in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    answer[i-1] = temp[j-1]
    answer[j-1] = temp[i-1]
    temp = answer.copy()

for z in answer:
    print(z, end=' ')
