import sys
input = sys.stdin.readline

a1, a0 = map(int, input().rstrip().split())
c = int(input().rstrip())
n0 = int(input().rstrip())

# a1, a0는 음수가 될 수 있다. 그런데 부등식을 정리했을 때, 무조건 a1이 c보다 작거나 같아야, 주어진 n0보다 큰 모든 양의 상수 n에 대하여 부등식을 만족하게 된다.
# 반례) a1=3, a0=-1, c=2, n0=1 일때
# 반례 설명) 3n-1 <= 2n이고 이를 정리하면, n <= 1이다. 즉 n은 1일때만 만족한다. 그런데 O(n)정의를 만족하려면 1(=n0)보다 큰 모든 양의 정수에 대해 만족해야 하는데, 2부터는 만족하지 않으므로 이는 0을 출력해야 정답이다.
# 그런데 n=1일때 만족하므로, 1을 출력하므로 (a1<=c) 조건을 넣어주게 되면 무조건 만족하게 된다.
if ((a1*n0) + a0) <= ((c*n0)) and (a1<=c):
    print(1)
else:
    print(0)
