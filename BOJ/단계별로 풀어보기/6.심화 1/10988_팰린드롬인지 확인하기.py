N = input()
N_back = N[::-1]

if N == N_back:
    print(1)
else:
    print(0)


"""
data = input()
reversed_data = reversed(data)

if data == reversed_data:
    print(1)
else:
    print(0)
"""

"""
def pelindrome(data):
    for i in range(len(data)):
        if data[i] != data[len(data) - i - 1]:
            return False
    return True

data = input()

if pelindrome(data):
    print(1)
else:
    print(0)
"""

'''
data = input()
reversed_data = data[::-1] # 이 코드는 많이 쓰임
# data[2:5] == [data[2], data[3], data[4]]
# data[2:5:-1] == [data[4], data[3], data[2]]
# data[:] == data
# data[::-1] == reversed(data)
# (start, end, step)

if data == reversed_data:
    print(1)
else:
    print(0)
'''
