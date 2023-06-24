import sys

ref = {
  'A+': 4.5,
  'A0': 4.0,
  'B+': 3.5,
  'B0': 3.0,
  'C+': 2.5,
  'C0': 2.0,
  'D+': 1.5,
  'D0': 1.0,
  'F': 0.0
}

answer = []
score_list = []
for i in range(20):
    subject, score, grade = sys.stdin.readline().rstrip().split()
    if grade == 'P':
        pass
    else:
        answer.append(float(score)*ref[grade])
        score_list.append(float(score))

print(sum(answer)/sum(score_list))
