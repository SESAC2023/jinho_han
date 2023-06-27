import sys
input = sys.stdin.readline

end = 1
answer = []
cnt = 0

while end > 0:
    A, B = map(int, input().rstrip().split())
    if A + B == 0:
        break
  
    if B%A == 0:
        answer.append('factor')
    elif (A%B==0):
        answer.append('multiple')
    else:
        answer.append('neither')
    cnt += 1
    
for i in range(cnt):
    print(answer[i])
