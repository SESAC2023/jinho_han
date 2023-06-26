import sys

students = set([i for i in range(1, 31)])
student = []

for i in range(28):
    student.append(int(sys.stdin.readline().rstrip()))


answer = list(students - set(student))
answer.sort()

for j in answer:
    print(j)
