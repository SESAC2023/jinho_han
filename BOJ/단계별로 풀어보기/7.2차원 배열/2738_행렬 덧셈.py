import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
data1 = []
data2 = []

for i in range(1, 2*N+1):  # 입력 받는 것 때문에 계속 틀렸었음. 여기가 중요
    if i > N:
        data2.append(list(map(int, sys.stdin.readline().rstrip().split())))
    else:
        data1.append(list(map(int, sys.stdin.readline().rstrip().split())))
      
for j in range(N):
    for k in range(M):
        print(data1[j][k]+data2[j][k], end=' ')
    if j<N-1:  
        print()
