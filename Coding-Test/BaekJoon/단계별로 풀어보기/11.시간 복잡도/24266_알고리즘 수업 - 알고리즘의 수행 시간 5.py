import sys
input = sys.stdin.readline

n = int(input().rstrip())

print(pow(n, 3))  # 수행횟수 = n^3
print(3)          # 시간 복잡도는 O(N^3)이므로 최고차항의 수는 3 이다.
