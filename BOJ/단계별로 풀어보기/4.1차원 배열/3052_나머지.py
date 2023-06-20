import sys

answer = []
for i in range(10):
    answer.append(int(sys.stdin.readline().rstrip())%42)

answer = len(list(set(answer)))
print(answer)
