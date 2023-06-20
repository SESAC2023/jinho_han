import sys

N = int(input())
scores = list(map(int, sys.stdin.readline().rstrip().split()))

score_max = max(scores)    # 문제 규칙을 위해 최대값 추출
score_fake = []            # 조작한 점수를 담기 위한 리스트 생성

for score in scores:       # 학생 점수가 담긴 리스트에서 점수를 하나씩 가져옴
    score_fake.append(score/score_max*100)  # 문제 규칙에 따라 "점수/최대점수*100"으로 바꾸고, 조작한 점수 리스트에 담기

print(sum(score_fake)/N)   # 조작한 점수 총합 / 점수 갯수 = 평균
