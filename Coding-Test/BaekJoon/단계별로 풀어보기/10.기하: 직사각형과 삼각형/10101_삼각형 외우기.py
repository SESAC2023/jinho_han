import sys
input = sys.stdin.readline

data = []
for i in range(3):
    data.append(int(input().rstrip()))


if sum(data) != 180:
    print('Error')
elif (data[0] == 60) and (data[0] == data[1]) and (data[1] == data[2]):
    print('Equilateral')
elif (data[0] == data[1]) or (data[0] == data[2]) or (data[1] == data[2]):
    print('Isosceles')
else:
    print('Scalene')
