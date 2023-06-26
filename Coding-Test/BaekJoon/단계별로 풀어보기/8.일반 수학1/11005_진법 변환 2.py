import sys
input = sys.stdin.readline
N, B = map(int, input().split())

share = N            # share = 몫
remain_list = []     # remain = 나머지  ->  나머지를 담을 리스트 생성

while share > 0:                  # 몫이 0이 될 때까지 나눈다.
    remain = share % B            # 먼저 나머지를 구하고
    remain_list.append(remain)    # 리스트에 차례로 담는다. (10진법 수를 B진법으로 출력하기 위해서)
    share //= B                   # 몫을 update

for i in remain_list[::-1]:       # B진법으로 출력하는 방법은 나머지를 거꾸로 출력하는 것이다.
    if i >= 10:                   # 10이상인 B진법으로 나타낼 때,
        print(chr(i+55), end='')  # 10 ~ 35까지는(B<=36) A ~ Z로 나타낸다.
    else:
        print(i, end='')          # 10보다 작은 수는 그대로 정수로 나타낸다.
