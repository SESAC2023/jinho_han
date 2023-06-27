import sys
input = sys.stdin.readline

N = int(input().rstrip())
data = list(map(int, input().rstrip().split()))

answer = []
for num in data:
    cnt = 0
    if num == 1:   # 1은 소수가 아님
        pass
    else:
        for i in range(2, num):   # 소수를 찾기 위해, 해당 숫자를 '2 ~ (해당숫자-1)'까지의 숫자로 하나씩 나눠본다.
            if num % i == 0:      # 만약 나눠지는 숫자가 있다면
                cnt += 1          ## cnt에 더한다.
            else:                 ## 안나누어 지면
                pass              ## 그 다음으로 넘어감
        if cnt > 0:               # for문이 모두 돌고나서, cnt > 0이면 2부터 (해당숫자-1)까지 나눠지는 숫자가 하나라도 있으므로
            pass                  ## 소수가 아니다. 그래서 answer 리스트에 추가하지 않는다. (소수가 아니므로)
        else:
            answer.append(num)    ## cnt = 0이라면 그 사이에 나눠지는 숫자가 없는 것이므로 소수이다. 그러므로 answer 리스트에 추가한다.

print(len(answer))                 # 소수의 갯수를 출력하는 것이 답이다.
