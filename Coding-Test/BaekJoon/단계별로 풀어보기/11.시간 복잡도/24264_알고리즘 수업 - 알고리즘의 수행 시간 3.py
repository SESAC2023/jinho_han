import sys
input = sys.stdin.readline

n = int(input().rstrip())

print(pow(n,2))  # '코드1'의 수행횟수는 n^2만큼 이루어 진다.
print(2)         # 시간 복잡도가 O(x * N^2)인데 상수는 필요 없으므로, 최고 차수는 2이다.
