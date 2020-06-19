import random
n = int(input('Enter a num: '))
a = int(input('Input diapozon: '))
b = int(input('Input diapozon: '))
lis = []
for i in range(n):
    lis.append(random.randint(a, b))
print(lis)
# while k < 2:
#     i = n - 1
#     check = lis[i]
#     while i > 0:
#         lis[i] = lis[i-1]
#         i -= 1
#     lis[i] = check
#     k += 1
new = []
k = 2
for i in range(k):
    new.append(lis[n-k+i])
for i in range(n-k):
    new.append(lis[i])
print(new)
