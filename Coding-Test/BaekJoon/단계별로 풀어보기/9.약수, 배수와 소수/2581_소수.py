import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

answer = []
for num in range(N, M+1):
    tmp = 0
    if num == 1:
        pass
    else:
        for i in range(2, num):
            if num % i == 0:
                tmp += 1
            else:
                continue
        if tmp > 0:
            pass
        else:
            answer.append(num)

if len(answer) > 0:
    print(sum(answer))
    print(min(answer))
else:
    print(-1)
