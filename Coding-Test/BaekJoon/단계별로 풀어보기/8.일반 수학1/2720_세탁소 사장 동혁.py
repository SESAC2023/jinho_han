import sys
input = sys.stdin.readline

T = int(input().rstrip())
answer = []

for _ in range(T):
    data = int(input().rstrip())
    tmp = [0] * 4                   # 25 or 10 or 5 or 1로 더이상 나누어 지지 않으면, 0으로 채우기 위해서 애초에 원소를 0으로만 가지는 리스트 생성

    while data > 0:                   
        if data // 25 > 0:          # 25로 나뉠 때까지
            tmp[0] = data // 25
            data %= 25
        elif data // 10 > 0:        # 10으로 나뉠 때까지
            tmp[1] = data // 10
            data %= 10
        elif data // 5 > 0:         # 5로 나뉠 때까지
            tmp[2] = data // 5
            data %= 5
        elif data // 1 > 0:         # 1로 나뉠 때까지
            tmp[3] = data // 1
            data %= 1
    answer.append(tmp)              

for i in answer:
    for j in i:
        print(j, end = ' ')         # 출력형식에 맞게
    print()
