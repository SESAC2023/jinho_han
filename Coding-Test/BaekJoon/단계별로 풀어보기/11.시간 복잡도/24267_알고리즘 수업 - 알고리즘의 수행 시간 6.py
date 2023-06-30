import sys
input = sys.stdin.readline

n = int(input().rstrip())

'''
수행횟수

i = 1 일때, j = 2 일때, k = 3~n => (n-2) 개
           j = 3 일때, k = 4~n => (n-3) 개
           ...
           j = n-1 일때, k = n~n => 1개              => (n-2)(n-1)/2 개

i = 2 일때, j = 3 일때, k = 4~n => (n-3) 개
           j = 4 일때, k = 5~n => (n-4) 개
           ...
           j = n-1 일때, k = n~n => 1개              => (n-3)(n-2)/2 개
...

i = n-3 일때, j = n-2 일때, k = n-1~n => 2개
             j = n-1 일때, k = n~n => 1개              => 2(2+1)/2 개
           
i = n-2 일때, j = n-1 일때, k = 4~n => (n-3) 개         => 1 개

'''

sum = 0
for i in range(1, n-2+1):
    sum += (n-(i+1)) * (n-i) / 2

print(int(sum))    # 규칙성을 찾아라. i=1일때 => 1 부터 (n-i-1)=(n-2) 까지의 합이 i=1일때의 시행횟수
                   #              i=2일때 => 1 부터 (n-i-1)=(n-3) 까지의 합이 i=2일때의 시행횟수
                   #              ...
                   #              i=n-2일때 => 1부터 (n-(n-2)-1)=1 까지의 합이 i=n-2일때의 시행횟수
                   # 즉 n-2만큼의 반복하면서 각각의 시행횟수를 더해주면 총 시행횟수가 나온다.

print(3)           # 시간 복잡도는 3차항을 가지므로 최고차항 수는 3 이다.
