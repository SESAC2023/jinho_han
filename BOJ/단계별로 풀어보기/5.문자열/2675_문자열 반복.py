import sys
N = int(input())

for i in range(N):
    re_num, string = sys.stdin.readline().rstrip().split()
    for j in string:  # 주어진 문자열을 하나씩 받아옴
        print(j*int(re_num), end='')  # 받아온 문자열을, 반복 숫자 만큼 반복
    print()
