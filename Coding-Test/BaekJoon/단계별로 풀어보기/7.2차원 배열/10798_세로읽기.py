import sys

data = []
len_list = []        # 각 입력마다 길이가 다르기 때문에, 입력 중 최대 길이 만큼 반복하기 위해 입력마다 길이를 받을 리스트 생성

for _ in range(5):
    tmp = list(sys.stdin.readline().rstrip())    # 입력 받음
    tmp2 = []                                    # 한 줄마다 받아온 데이터에서 알파벳별로 리스트를 담기 위해 임시 리스트 생성
    for i in tmp:                                # 알파벳 하나씩 받아옴
        tmp2.append(i)                           # 임시 리스트 tmp2에 알파벳 하나씩 담아서
    data.append(tmp2)                            # data 리스트에 담아서 2차원 배열을 만든다.
    len_list.append(len(tmp2))                   # 2차원 배열의 원소마다 리스트 길이를 담는다.


sum = ''                             # 알파벳을 공백 없이 합치기 위해 생성
for j in range(max(len_list)):
    for list in data:                # data는 2차원 배열이고, 그 안에 원소 자체도 리스트이다. 즉 list라는 변수에 리스트가 들어 있다.
        try:                         # 입력 데이터 길이가 모두 달라서 공백이 있는 입력이 있을 수 있음. 그래서 우선 알파벳 합치기를 시도하고
            sum += list[j]
        except:                      # 오류가 나면 무시하고
            continue                 # 현재 돌고 있는 for문 처음으로 다시 돌아간다.

print(sum)
