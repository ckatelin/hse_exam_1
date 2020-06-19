def new_dic(ori, des, names):
    fd = open(ori + '-' + des + '.csv', 'w')
    for i in range(2, len(names)-1):
        fd.write(names[i]+',')
    i += 1
    fd.write(names[i] + '\n')
    fd.close()
    # fd = open(ori + '-' + des + '.csv', 'r')
    # i = fd.readline().split(',')
    # print(i)
    # fd.close()

def ft_console():
    ori = str(input('Enter origin: '))
    des = str(input('Enter destination: '))
    date = str(input('Enter date in the YYYY-MM-DD format :'))
    return ori, des, date

fd = open("./TrainTickets/source/renfe.csv")
mas = fd.readline().split(',')
dic = {}
names = []
cities = []
mas[len(mas) - 1] = mas[len(mas) - 1][0:-1]
for i in range(2, len(mas)):
    dic[mas[i]] = []
    names.append(mas[i])
# print(names)
# print(dic)
for j in fd:
    mas = j.split(',')
    if mas[2] not in cities:
        cities.append(mas[2])
    if mas[3] not in cities:
        cities.append(mas[3])
    for i in range(2, len(mas)):
        dic[names[i-2]].append(mas[i])
fd.close()
for i in range(1, len(cities)):
    new_dic(cities[0], cities[i], names)
    new_dic(cities[i], cities[0], names)
for i in range(len(dic[names[0]])):
    t = True
    fd = open(dic[names[0]][i] + '-' + dic[names[1]][i] + '.csv', 'r')
    fd.readline()
    for j in fd:
        f = j.split(',')
        if dic[names[2]][i] == f[0]:
            t = False
            break
    fd.close()
    if t:
        fd = open(dic[names[0]][i] + '-' + dic[names[1]][i] + '.csv', 'a')
        for j in range(2, len(names) - 1):
            fd.write(dic[names[j]][i] + ',')
        fd.write(dic[names[j + 1]][i])
        fd.close()


ori, des, date = ft_console()
while ori not in cities or des not in cities:
    print('\n' * 100)
    ori, des, date = ft_console()
# ori = 'SEVILLA'
# des = 'MADRID'
# date = '2019-04-19'
fd = open(ori + '-' + des + '.csv', 'r')
fd.readline()
for f in fd:
    i = f.split(',')
    k = i[0].split(' ')
    if k[0] == date:
        print(ori + ' - ' + des + ':', end=' ')
        for j in range(len(i) - 1):
            print(i[j], end=', ')
        print(i[5])
fd.close()

