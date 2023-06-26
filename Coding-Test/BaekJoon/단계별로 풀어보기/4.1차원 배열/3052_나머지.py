import sys

answer = []
for i in range(10):
    answer.append(int(sys.stdin.readline().rstrip())%42)

answer = len(list(set(answer)))
print(answer)


'''
- 1번 솔루션
arr = []

for i in range(10):
    x = int(input())
    arr.append(x % 42)

print(len(set(arr)))


- 2번 솔루션
data = set()

for i in range(10):
    x = int(input())
    data.add(x % 42)

print(len(data))
'''
