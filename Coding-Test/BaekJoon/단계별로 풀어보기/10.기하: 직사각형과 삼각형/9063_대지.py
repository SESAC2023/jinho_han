import sys
input = sys.stdin.readline

N = int(input().rstrip())

data = []
x = []
y = []

for i in range(N):
    xy = tuple(map(int, input().rstrip().split()))
    x.append(xy[0])
    y.append(xy[1])
    data.append(xy)

print((max(x) - min(x)) * (max(y) - min(y)))
