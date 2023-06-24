'''
# 해당 문제 아이디어
1) 알파벳 방문 여부를 확인
2) 방문한 적이 없는 알파벳이라면, 방문처리
3) 방문한 적이 있다면, 해당 알파벳 위치의 이전 인덱스 자리에 똑같은 알파벳이 아니라면 '실패'로 인식
'''

def group(string):
    chars = [False] * 26              # 각 알파벳에 대한 방문 여부
    for i in range(len(string)):      # 주어진 단어(입력)를 하나씩 살펴봐야 함
        x = ord(string[i]) - 97       # 소문자 a는 유니코드 10진수로 97이므로, a=0
        
        # 방문한 적 없는 알파벳이라면
        if not chars[x]:
            chars[x] = True           # 해당 알파벳이 나왔었다는 의미 => 방문 처리
        
        # 방문한 적 있는 알파벳이라면
        else:
            # (중요!) 직전 알파벳이랑 다르다면 그룹 단어 아님
            if string[i] != string[i - 1]:
                return False
    return True  # 위에서 False가 return 되지 않는다면, 그룹단어이므로 True 반환


N = int(input())
cnt = 0                # 그룹단어 갯수를 출력하는 것이 문제
for i in range(N):
    string = input()   # 여러 개 단어 받자
    if group(string):  # group이라는 함수에서 True를 반환하면
        cnt += 1       # 그룹 단어이므로, 카운트 하자.
print(cnt)
