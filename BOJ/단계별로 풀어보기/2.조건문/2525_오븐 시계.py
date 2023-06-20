import sys

A, B = map(int, sys.stdin.readline().rstrip().split())
time = int(sys.stdin.readline().rstrip())

if B+time<60:
    print(A, B+time)
elif B+time>=60:
    H = A+((B+time)//60)
    M = (B+time)%60
    if H>=24:
        print(H-24, M)
    else:
        print(H, M)
