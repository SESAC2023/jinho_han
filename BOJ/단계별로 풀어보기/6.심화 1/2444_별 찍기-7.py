N = int(input())

for i in range(1, 2*N):
    if i>(2*N)//2:        # 주어지는 숫자 N에 따라 2*N의 반절이 넘어가면서 부터는 별의 갯수가 줄어들어야 한다.
        print(' '*(i-N) + ((2*N-i)*2-1)*'*')
    else:
        print(' '*(N-i) + (2*i-1)*'*')
