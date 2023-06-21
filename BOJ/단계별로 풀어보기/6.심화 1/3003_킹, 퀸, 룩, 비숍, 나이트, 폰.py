data = list(map(int, input().split()))
correct = [1, 1, 2, 2, 2, 8]  # 킹, 퀸, 룩, 비숍, 나이트, 폰의 올바른 갯수

answer = []
for i in range(len(correct)):
    answer.append(correct[i] - data[i])

for j in answer:
    print(j, end=' ')
