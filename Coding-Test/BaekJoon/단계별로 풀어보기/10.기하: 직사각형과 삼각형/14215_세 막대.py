import sys
input = sys.stdin.readline

data = list(map(int, input().rstrip().split()))
answer = []

tmp = data.copy()
tmp_max = max(tmp)    
tmp.remove(max(data))  
total = sum(tmp)        
 
if max(data) < total:
    print(sum(data))
else:
    while total <= tmp_max:
        tmp_max -= 1
        if tmp_max < total:
            tmp.append(tmp_max)
            break
    print(sum(tmp))
