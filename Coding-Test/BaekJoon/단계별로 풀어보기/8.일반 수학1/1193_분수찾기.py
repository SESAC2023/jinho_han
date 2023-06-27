'''
# 이 문제의 가장 큰 규칙은 n라인에는 n개의 분자가 있다는 것이다. 그 다음,
- 짝수라인은 시작점에서 끝점으로 갈수록 분자가 1씩 늘어가고 분모가 1씩 감소하며
- 홀수라인은 시작점에서 끝점으로 갈수록 분자가 1씩 줄어들고 분모가 1씩 늘어나는 형태임을 파악할 수 있다.
- 즉, 이 문제는 내가 구하고자 하는 수가 몇번째 라인에 있는지, 그 중에서 "몇 번째 인덱스"에 있는지 알면 된다.
'''

import sys
input = sys.stdin.readline

N = int(input().rstrip())

line = 0
end = 0

while N > end:               # line 숫자만큼 끝 인덱스가 계속해서 바뀌므로!
    line += 1                ## while문을 돌때마다 line이 바뀜
    end += line              ## line번째 줄은 갯수가 line개 만큼 있음
                             ### 여기서 end는 해당 line의 마지막 index를 뜻함

diff = end - N               # diff: 해당 line에서 n번째 분수와, 해당 line의 끝 분수 index와의 차이를 나타냄
                             ## 이 차이를 이용해서 해당 line의 분자를 구할 수 있음

if line%2 == 0:              # 짝수 라인 일때, 시작점에서 끝점으로 갈수록 분자가 1씩 늘어가고, 분모가 1씩 감소하므로
    top = line - diff        ## 분자는 "해당 line - diff(n번째 분수와 해당 line 끝 분수의 index 차이)"를 통해 구할 수 있음
    bottom = diff + 1        ## 분모는 diff에 1씩 더하면 구할 수 있음        

else:                        # 홀수 라인 일때, 시작점에서 끝점으로 갈수록 분자가 1씩 줄어들고, 분모가 1씩 늘어나므로
    top = diff + 1           ## 분자는 diff에 1씩 더하면 구할 수 있음
    bottom = line - diff     ## 분모는 "해당 line - diff(n번째 분수와 해당 line 끝 분수의 index 차이)"를 통해 구할 수 있음

print("%d/%d"%(top,bottom))


'''
ex) N이 8일때

1) line=1, end=1
2) line=2, end=3
3) line=3, end=6
4) line=4, end=10

diff = end(해당 line의 끝 index) - N(분수 위치) = 10 - 8 = 2
이 차이(diff)와, 짝수일떄 분자/분모의 규칙성 & 홀수일때 분자/분모의 규칙성을 이용하면 쉽게 구할 수 있음
'''
