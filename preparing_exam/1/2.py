name = str(input('Input  str: '))
matrix = str(input('Matrix: '))
s = 0
t = True
while True:
    s = 0
    for i in range(len(matrix)):
        if (matrix[i] >= '0' and matrix[i] <= '9') or matrix[i] == 'x':
            if matrix[i] == 'x' and s == 0:
                s += 1
            elif (matrix[i] >= '0' and matrix[i] <= '9'):
                t = True
            else:
                t = False
                break
            t = True
        else:
            t = False
            break
    if t and s == 1:
        break
    matrix = str(input('Matrix good!: '))
i = 0
n1 = ''
while matrix[i] != 'x':
    n1 += matrix[i]
    i += 1
i += 1
n2 = ''
while i < len(matrix):
    n2 += matrix[i]
    i += 1
n = int(n1)
m = int(n2)
print(n, m)
for i in range(n):
    for j in range(m):
        if i + j * n < len(name):
            print(name[i + j*n], end=' ')
        else:
            print('-', end=' ')
    print('')
