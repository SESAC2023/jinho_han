def group(string):
    # 각 알파벳에 대한 방문 여부
    chars = [False] * 26
    for i in range(len(string)):
        x = ord(string[i]) - 97
        # 방문한 적 없는 알파벳이라면
        if not chars[x]:
            chars[x] = True # 방문 처리
        # 방문한 적 있는 알파벳이라면
        else:
            # 직전 알파벳이랑 다르다면 그룹 단어 아님
            if string[i] != string[i - 1]:
                return False
    return True

n = int(input())
cnt = 0
for i in range(n):
    string = input()
    if group(string):
        cnt += 1
print(cnt)
