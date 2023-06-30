import sys
input = sys.stdin.readline


N = 0         # 총 테스트 데이터 갯수 알기 위해서
answer = []   # 답 출력을 위해

while(1):     # 데이터 합이 0이 될 때까지 반복문 돌리기 위해 무한 반복 하고 아래 break 만나면 멈춤
    data = list(map(int, input().rstrip().split()))
    tmp_data = data.copy()
    
    if sum(data) == 0:   # 데이터 합이 0이면 끝
        break

    N += 1
    tmp_data.remove(max(tmp_data))
      
    if max(data) >= sum(tmp_data):
        answer.append('Invalid')
        continue
      
    if (data[0] == data[1]) and (data[1] == data[2]):
        answer.append('Equilateral')
    elif (data[0] == data[1]) or (data[0] == data[2]) or (data[1] == data[2]):
        answer.append('Isosceles')
    elif (data[0] != data[1]) and (data[1] != data[2]):
        answer.append('Scalene') 
    

for i in range(N):
    print(answer[i])
