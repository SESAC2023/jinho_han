import sys
input = sys.stdin.readline

end = 1
answer = []
cnt = 0

while end > 0:
    N = int(input().rstrip())
    if N < 0:
        break
      
    tmp = []
    for i in range(1, N+1):  
        if N % i == 0:
            tmp.append(i)
    tmp = tmp[0:(len(tmp)-1)]
          
    if N == sum(tmp):
        output = '{0} ='.format(N)
        for j in range(len(tmp)):
            if j == len(tmp) - 1:
                output += ' ' + str(tmp[j])
            else:
                output += ' ' + str(tmp[j]) + ' +'
        answer.append(output)
    else:
        answer.append('{0} is NOT perfect.'.format(N))

    cnt += 1


for k in range(cnt):
    print(answer[k])
