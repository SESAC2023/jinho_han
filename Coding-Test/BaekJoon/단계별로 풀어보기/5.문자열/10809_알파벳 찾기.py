S = input()
data = [i for i in S]   # 문자열은 슬라이싱 할 수 있으므로, 컴프리헨션을 통해 개별 알파벳을 원소로하는 리스트 생성

lower_str = [chr(i) for i in range(97,123)]  # 알파벳 소문자 아스키코드(10진수)를 알고 있으므로, 소문자 a ~ z까지 리스트 생성 (각 알파벳이 단어에 들어있는지 확인하기 위해서)
for i in lower_str:   # 알파벳 하나씩 가져옴
    if i in data:     # 주어진 단어(데이터) 안에 알파벳이 있다면
        print(data.index(i), end=' ')  # 가장 처음에 있는 인덱스 반환 (index 함수는 여러 개 있어도, 가장 첫번째 인덱스를 반환)
    else:
        print(-1, end=' ')             # 없다면 -1 반환
