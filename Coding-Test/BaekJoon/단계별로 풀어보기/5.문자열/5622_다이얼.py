data = input()

temp = []
for j in data:
    if j in ['A', 'B', 'C']:
        temp.append(3)
    elif j in ['D', 'E', 'F']:
        temp.append(4)
    elif j in ['G', 'H', 'I']:
        temp.append(5)
    elif j in ['J', 'K', 'L']:
        temp.append(6)
    elif j in ['M', 'N', 'O']:
        temp.append(7)
    elif j in ['P', 'Q', 'R', 'S']:
        temp.append(8)
    elif j in ['T', 'U', 'V']:
        temp.append(9)
    elif j in ['W', 'X', 'Y', 'Z']:
        temp.append(10)

print(sum(temp))
