s = str(input())
n = s.split(' ')
x = []
k = 0
for i in range(len(n)):
    if n[i][len(n[i])-1] == '.':
        n[i] = n[i][0:-1]
    try:
        x.append(float(n[i]))
    except ValueError:
        k += 1
min = x[0]
for i in range(len(x)):
    if x[i] < min:
        min = x[i]
print(min)
