import sys

num = []
for i in range(9):
    num.append(int(sys.stdin.readline().rstrip()))

print(max(num))
print(num.index(max(num))+1)
