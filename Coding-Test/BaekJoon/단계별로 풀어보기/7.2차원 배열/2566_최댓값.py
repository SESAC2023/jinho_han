import sys

data = []
index = {}
answer = []

for i in range(9):
    data.append(list(map(int, sys.stdin.readline().rstrip().split())))
    index[i+1] = (max(data[i]), data[i].index(max(data[i]))+1)          # 1) 행 인덱스를 key로 하고, (해당 행에서 최댓값, 그 최댓값의 열 인덱스) 튜플을
                                                                        #    value로 하는 index 딕셔너리를 생성


for j in range(9):
    answer.append(list(index.values())[j][0])    # 위에서 만든 index라는 딕셔너리에서 튜플 value들을 리스트로 만들고, 거기서 행마다의 최댓값을
                                                 # 가져와서 리스트에 넣는다.


for key, val in index.items():                   # 딕셔너리의 items() 함수를 통해, key와 value를 뽑아오고 
    if val[0] == max(answer):                    # 튜플로 구성된 value에서 값을 나타내는 첫 번째(0 index) 원소가 전체 행렬에서 최댓값(max(answer))이 보이면
        print(val[0])                            # 그 때의 최댓값을 출력하고
        print(key, val[1])                       # 이때의 key(행 인덱스, 1부터 시작)와 튜플로 구성된 value중 2번째 원소(1 index)인 열 인덱스를 추출
        break                                    # 구하면 멈추자
    else:
        continue                                 # 최댓값이 안나왔다면 다시 for문을 이어서 실행하라
