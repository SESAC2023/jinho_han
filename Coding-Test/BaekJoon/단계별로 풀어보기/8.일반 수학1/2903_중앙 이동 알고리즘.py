'''
이 문제는 수의 규칙을 찾으면 된다.
'''

import sys
input = sys.stdin.readline

N = int(input().rstrip())

a = 3
for i in range(1, N+1):
    answer = pow(a, 2)
    a += 2**i

'''
N = 1  ->  3^2                   = 9
N = 2  ->  5^2   = (3 + 2^1)^2   = 25
N = 3  ->  9^2   = (5 + 2^2)^2   = 81
N = 4  ->  17^2  = (9 + 2^3)^2   = 289
N = 5  ->  33^2  = (17 + 2^4)^2  = 1089
'''

print(answer)
