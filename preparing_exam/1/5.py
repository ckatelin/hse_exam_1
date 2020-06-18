s = str(input())
n = s.split(' ')
min = n[0]
m = []
sum = 0
for i in range(len(n)):
    if n[i] < min:
        min = n[i]
for i in range(len(n)):
    if n[i] == min:
        m.append(i)
if len(m) <= 1:
    print('One min or no elements')
else:
    if m[len(m)-1] - m[0] == 1:
        print('No el between')
    else:
        for i in range(m[0] + 1, m[len(m) - 1]):
            sum += int(n[i])
        print(sum)




