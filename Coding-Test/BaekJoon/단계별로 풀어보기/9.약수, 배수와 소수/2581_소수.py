import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

answer = []
for num in range(N, M+1):
    tmp = 0
    if num == 1:
        pass
    else:
        for i in range(2, num):
            if num % i == 0:
                tmp += 1
            else:
                continue
        if tmp > 0:
            pass
        else:
            answer.append(num)

if len(answer) > 0:
    print(sum(answer))
    print(min(answer))
else:
    print(-1)


""" Solution 2: 제곱근까지만 보기(더 효율적)
import sys
import math
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

# x = int(input())


# x가 소수인지 알려주는 함수
# 소수란? 1과 자기 자신을 제외하고는 나누어 떨어지지 않는 수
def is_prime(x):  # 최악의 경우 시간 복잡도: O(x)
    if x == 1: return False  # 1은 소수가 아님
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:  # 나누어 떨어지면
            return False  # 소수가 아님
    return True  # 소수임


m = int(input())
n = int(input())

summary = 0  # 소수의 합
min_value = int(1e9)  # 소수 중에 가장 작은 값
for x in range(m, n + 1):  # 전체 시간 복잡도: O(N^2)
    if is_prime(x):  # x가 소수라면
        summary += x  # 소수의 합 계산
        if min_value == int(1e9):  # 최솟값 기록
            min_value = x

if summary == 0:  # m와 n 중간에 소수가 없는 경우
    print(-1)
else:
    print(summary)
    print(min_value)
"""
