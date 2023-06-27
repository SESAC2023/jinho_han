'''
해당 문제는 파이썬에는 유리하다.
파이썬은 잧적으로 큰 수를 지원하기 때문이다. 하지만 다른 언어들은 그렇지 않으므로, 다른 언어들을 위한 문제가 되겠다.
이 문제는 파이썬에서는 단순히 print(A+B)가 맞다.
'''

import sys
input = sys.stdin.readline

A, B = map(int, input().rstrip().split())

print(A+B)
