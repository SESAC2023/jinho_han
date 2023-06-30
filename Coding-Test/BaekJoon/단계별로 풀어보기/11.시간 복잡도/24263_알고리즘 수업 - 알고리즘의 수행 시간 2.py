import sys
input = sys.stdin.readline

n = int(input().rstrip())

print(n)   # 코드1의 수행횟수는 n번이다.
print(1)   # 시간복잡도는 O(x * N)인데 상수는 필요없으므로 O(N)이다.
