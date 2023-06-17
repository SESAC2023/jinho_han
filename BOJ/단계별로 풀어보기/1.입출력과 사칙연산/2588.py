a = int(input())
b = input()

B = list(map(int, b))

I, J, K = a * B[-1], a * B[-2], a * B[-3]

print(I)
print(J)
print(K)
print(a * int(b))
