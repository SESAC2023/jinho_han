import sys
input = sys.stdin.readline

n = int(input().rstrip())

'''
i = 1 일때, j = 2~n 으로 => n-1개
i = 2 일때, j = 3~n 으로 => n-2개
...
i = n-2 일때, j = n-1~n 로 => 2개
i = n-1 일때, j = n~n 로 => 1개

즉 연산의 수 = 1 + 2 + ... + (n-2) + (n-1) = (n-1) * n / 2 = (n^2 - n) / 2
'''

print(int((pow(n,2) - n)/2))   # 연산 수 = (n^2 - n) / 2
print(2)                       # 시간 복잡도는 O( (n^2 - n)/2 )이므로 최고차항의 수는 2 이다.
