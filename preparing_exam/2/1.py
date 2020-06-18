def new_dic(ori, des, names):
    fd = open(ori + '-' + des + '.csv', 'w')
    for i in range(len(names)-1):
        fd.write(names[i]+',')
    i += 1
    fd.write(names[i] + '\n')
    fd.close()
    # fd = open(ori + '-' + des + '.csv', 'r')
    # i = fd.readline().split(',')
    # print(i)
    # fd.close()


fd = open("./TrainTickets/source/renfe.csv")
mas = fd.readline().split(',')
dic = {}
names = []
cities = []
mas[len(mas) - 1] = mas[len(mas) - 1][0:-1]
for i in range(2, len(mas)):
    dic[mas[i]] = []
    names.append(mas[i])
print(names)
print(dic)
for j in fd:
    mas = j.split(',')
    if mas[2] not in cities:
        cities.append(mas[2])
    if mas[3] not in cities:
        cities.append(mas[3])
    for i in range(2, len(mas)):
        dic[names[i-2]].append(mas[i])
for i in range(1, len(cities)):
    new_dic(cities[0], cities[i], names)
    new_dic(cities[i], cities[0], names)
for i in range(len(dic[names[0]])):
    fd = open(dic[names[0]][i] + '-' + dic[names[1]][i] + '.csv', 'a')
    fd.write('check')
fd.close()
