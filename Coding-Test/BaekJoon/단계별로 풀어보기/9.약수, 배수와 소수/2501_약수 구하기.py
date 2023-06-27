import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

answer = []
for i in range(1, N+1):
    if N % i == 0:
        answer.append(i)

try:
    print(answer[K-1])
except:
    print(0)
