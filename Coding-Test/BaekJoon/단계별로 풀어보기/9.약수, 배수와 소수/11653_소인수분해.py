import sys
input = sys.stdin.readline

N = int(input().rstrip())

m = 2
while N != 1:  # N을 m으로 나눴을때 몫이 1이 되면 멈춤.
  if N%m==0: 
    print(m) 
    N = N//m
  else:
    m += 1   # 2부터 나누기 시작해서, 딱 나누어 떨어지지 않으면
             # 나누는 값인 m을 하나씩 증가시키면서 찾는다.
             # 어차피 N을 m으로 나눴을 때 나머지가 0이고, 몫이 1이 되는 순간 -> 그 숫자는 모두 나뉜 것이고,
             ## 더 이상 m과 1을 제외하고 나뉠 수가 없기 때문이다. 즉 모두 소수로 나뉘어진 것이다.
