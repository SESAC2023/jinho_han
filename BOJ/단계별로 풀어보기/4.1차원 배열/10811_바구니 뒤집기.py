import sys

N, M = map(int, sys.stdin.readline().split())
answer = [i for i in range(1, N+1)]

for j in range(M):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    temp = answer[start-1:end]    # 역순할 리스트 범위만큼 추출해서 임시 리스트에 저장 & 파이썬 인덱스는 0부터 시작 & 슬라이스는 끝 인덱스 미포함
    temp = temp[::-1]             # 추출한 리스트 역순. ([::-1]의미 -> [시작:끝:규칙]이므로 '전체 리스트에서 역순'으로 라는 의미)
    answer[start-1:end] = temp    # 파이썬 인덱스는 0부터 시작하므로 -1 & 슬라이는 끝 인덱스 미포함이므로 그대로 & 해당 인덱스에 그대로 삽입 => 인덱스 자리에 값이 교체됨

for k in answer:
    print(k, end=' ')             # 리스트 말고 띄어쓰기 된 숫자로 출력



''' 1번 풀이
n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]

for i in range(m);
    left, right = map(int, input().split())
    left -= 1
    arr[left:right] = reversed(arr[left:right])

for x in arr:
    print(x, end=' ')
'''


''' 2번 풀이
n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]

for i in range(m):
    left, right = map(int, input().split())
    left -= 1
    temp = []
    for j in range(left, right):
        temp.append(arr[j])
    for j in range(left, right):
        arr[j] = temp.pop()

for x in arr:
    print(x, end=" ")
'''
