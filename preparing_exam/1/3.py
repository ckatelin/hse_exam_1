matrix = str(input())
matrix = matrix.split(' ')
mas = []
mas.append(matrix)
for i in range(len(matrix)):
    matrix = str(input())
    matrix = matrix.split(' ')
    mas.append(matrix)
# while n != m:
#     print('Need square matrix')
#     n = int(input('Strings'))
#     m = int(input('Rows'))
# mas = []
# for i in range(n):
#     mas.append([])
#     s = str(input()).split(' ')
#     if len(s) != n:
#         print('not square')
#         exit()
#     for j in range(m):
#         mas[i].append(int(s[j]))
for i in range(len(mas[0])):
    for j in range(len(mas[0])):
        print(mas[i][j], end=' ')
    print()

s = 0
for i in range(len(mas[0])):
    for j in range(len(mas[0])):
        if i == j:
            s += int(mas[i][j])
print(s)

s = 0
for i in range(len(mas[0])):
    for j in range(len(mas[0])):
        if i + j == len(mas[0]) - 1:
            s += int(mas[i][j])
print(s)