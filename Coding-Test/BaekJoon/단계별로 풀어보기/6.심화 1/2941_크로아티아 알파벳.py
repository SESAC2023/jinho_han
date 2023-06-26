data = input()

count = 0
index = 0

while index < len(data) :  # 주어진 문자열 길이 보다, 슬라이싱하는 인덱스가 더 작을때 까지만 돌아가므로, 문자열 인덱스 범위를 넘어갈 일 없음

    # 먼저 2글자 단어부터 탐색
    if data[index : index+2] in ('c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z='): 
        count += 1   # 있다면 count 해주고
        index += 2   # 해당 단어 끝의 다음 인덱스로 인덱스 초기화
        continue     # 아래 코드를 실행하지 않고, 다시 while문 처음으로 돌아가서 다시 2글자 단어부터 탐색
    
    # 2글자에서 없다면, 3글자인 경우를 탐색
    elif data[index : index+3] == 'dz=':
        count += 1   # 있다면 count 해주고
        index += 3   # 해당 단어 끝의 다음 인덱스로 인덱스 초기화
        continue     # 아래 코드를 실행하지 않고, 다시 while문 처음으로 돌아가서 다시 2글자 단어부터 탐색

    # 1글자인 경우
    if data[index] not in ('-', '='):  # 알파벳 갯수면 세면 되고, '-'과 '='이 들어가면 우선 위에서 걸러질 것이기 때문에
        count += 1   # 알파벳에 해당 된다면 count 해주고
        index += 1   # 해당 알파벳 다음의 인덱스로 인덱스 초기화
        continue     # 아래 코드를 실행하지 않고, 다시 while문 처음으로 돌아가서 다시 2글자 단어부터 탐색

print(count)
