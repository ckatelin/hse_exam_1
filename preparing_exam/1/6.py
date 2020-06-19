import random

def check(mas, num):
    for i in range(len(mas)):
        if num in mas[i]:
            return False
    return True


n = int(input())
ran = str(input()).split(' ')
mas = []
for i in range(n):
    mas.append(random.randint(int(ran[0]), int(ran[1])))
# mas = str(input()).split(' ')  #  for example/ comment previous
k = int(input('k = '))
new = []
for i in range(k):
    new.append([])
for j in range(len(mas)):
    add = 0
    for c in range(j, len(mas)):
        if int(mas[j]) == int(mas[c]):
            add += 1
    if add <= k and check(new, int(mas[j])):
        new[add-1].append(int(mas[j]))
print(new)
