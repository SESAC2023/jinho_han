import sys
input = sys.stdin.readline

axes = []
for _ in range(3):
    xy = list(map(int, input().rstrip().split()))
    axes.append(xy)
    
x = []
y = []

for i in range(3):
    x.append(axes[i][0])
    y.append(axes[i][1])


x_unique = list(set(x))
y_unique = list(set(y))

x_num = []
y_num = []
for i in range(len(x_unique)):
    x_num.append((x_unique[i], x.count(x_unique[i])))
    y_num.append((y_unique[i], y.count(y_unique[i])))


if x_num[0][1] > x_num[1][1]:
    print(x_num[1][0], end=' ')
else:
    print(x_num[0][0], end=' ')

if y_num[0][1] > y_num[1][1]:
    print(y_num[1][0],end=' ')
else:
    print(y_num[0][0], end=' ')
