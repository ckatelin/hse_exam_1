n = int(input('Strings'))
m = int(input('Rows'))
while n != m:
    print('Need square matrix')
    n = int(input('Strings'))
    m = int(input('Rows'))
mas = []
for i in range(n):
    mas.append([])
    s = str(input()).split(' ')
    if len(s) != n:
        print('not square')
        exit()
    for j in range(m):
        mas[i].append(int(s[j]))

for i in range(n):
    for j in range(m):
        print(mas[i][j], end=' ')
    print()

s = 0
for i in range(n):
    for j in range(m):
        if i == j:
            s += mas[i][j]
print(s)

s = 0
for i in range(n):
    for j in range(m):
        if i + j == n-1:
            s += mas[i][j]
print(s)