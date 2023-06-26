data = list(map(int, input().split()))
data_unique = list(set(data))

if len(set(data)) == 1:
    print(10000+(data[0]*1000))
elif len(set(data)) == 2:
    print(1000 + 100*(sum(data)-sum(data_unique)))
elif len(set(data)) == 3:
    print(max(data)*100)
