import sys

a, b = sys.stdin.readline().rstrip().split()

a = a[::-1]
b = b[::-1]

if a > b:
    print(a)
elif a < b:
    print(b)
