import sys

total = int(input())
N = int(input())

sum = 0
for i in range(N):
    price, quant = map(int, sys.stdin.readline().rstrip().split())
    sum += price*quant

if total == sum:
    print('Yes')
else:
    print('No')
