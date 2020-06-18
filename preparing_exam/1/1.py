import random
n = int(input('Enter a num: '))
a = int(input('Input diapozon: '))
b = int(input('Input diapozon: '))
lis = []
for i in range(n):
    lis.append(random.randint(a, b))
print(lis)
i = n - 1
check = lis[i]

while i > 0:
    lis[i] = lis[i-1]
    i -= 1
lis[i] = check
print(lis)