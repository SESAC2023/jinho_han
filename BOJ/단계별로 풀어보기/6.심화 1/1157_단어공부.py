N = [i for i in input().upper()]   # 대문자로 출력해야 하므로, 애초에 모두 대문자로 변경
unique = list(set(N))              # 중복되는 알파벳은 하나로 봐야하므로 집합으로 나타낸 후, 리스트로 변환


temp = {}                          # 알파벳별로 갯수를 알기 위해 딕셔너리 생성   ex) M:2 => M은 2개
for i in unique:  
    temp[i] = N.count(i)           # 알파벳은 key가 되고, 그 갯수는 value가 되어 딕셔너리에 저장

temp_vals = list(temp.values())    # 딕셔너리의 값(value)만 모아서 리스트로 변환
temp_max = max(temp_vals)          # 바로 위에서 변환된 리스트 중에서 최대값 추출

if temp_vals.count(temp_max) >=2:  # 최대값(temp_max)이 2개 이상이면, 
    print('?')                     # 물음표(?) 반환
else:                              # 최대값(temp_max)이 1개만 있다면
    print([k for k, v in temp.items() if v == temp_max][0])  # 최대값에 맞는 key(알파벳)을 반환
