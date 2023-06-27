import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().rstrip().split())


distance = [x, w-x, y, h-y]
print(min(distance))
