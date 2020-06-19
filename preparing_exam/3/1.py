from utils import *
import os


LOG = 1
PAS = 2

ASK = '1 - tasks\n2 - new task\n3 - delete task\n4 - log out'

def ft_console(names, passwords):
    name = str(input("Name: "))
    password = get_hash(str(input('Password: ')))
    while name not in names:
        print('Not existed login')
        name = str(input("Name: "))
        password = get_hash(str(input('Password: ')))
    while password != passwords[name]:
        print(password)
        print('not right password, try again')
        password = get_hash(str(input('Password: ')))
    return name, password


def ft_get_id(names, name):
    for i in range(names):
        if name == names[i]:
            return i


def ft_add_work(fd, names, m, dic):
    for i in range(len(names)):
        dic[names[i]]['date'] = []
        dic[names[i]]['task'] = []
        dic[names[i]]['prior'] = []
    for i in range(m):
        k = fd.readline().split(';')
        print(k)
        if k[3][len(k[3]) - 1] == '\n':
            k[3] = k[3][0:-1]
        if k[3] == 'all':
            for f in dic:
                dic[f]['date'].append(k[0])
                dic[f]['task'].append(k[1])
                dic[f]['prior'].append(k[2])
        else:
            dic[k[3]]['date'].append(k[0])
            dic[k[3]]['task'].append(k[1])
            dic[k[3]]['prior'].append(k[2])
    return dic


def ft_console2(n):
    if n == '':
        exit()
    while n <= '0' or n > '4':
        if n == '\n':
            exit()
        int(input(ASK))
    return int(n)


def ft_main_cons(dic, names, passwords, name):
    n = ft_console2(str(input(ASK)))
    if int(n) == 1:  # КРАСИВЫЙ ВЫВОД!!!!!!!
        for d in dic[name]:
            if d != 'password':
                print('\33[1m{0:<40}'.format(d), end='')
        print()
        for i in range(len(dic[name]['date'])):
            print('\33[1m{0:<40}'.format(dic[name]['date'][i]), end='')
            print('\33[1m{0:<40}'.format(dic[name]['task'][i]), end='')
            print('\33[1m{0:<40}'.format(dic[name]['prior'][i]), end='')
            print('\33[0m{0:<40}'.format(''))
        ft_main_cons(dic, names, passwords, name)
    elif int(n) == 2:
        s1 = str(input('task'))
        s2 = str(input('date'))
        s3 = str(input('prior'))
        dic[name]['task'].append(s1)
        dic[name]['date'].append(s2)
        dic[name]['prior'].append(s3)
        if str(input('all? ')) == 'Y':
            for i in range(len(names)):
                if name != names[i]:
                    dic[names[i]]['task'].append(s1)
                    dic[names[i]]['date'].append(s2)
                    dic[names[i]]['prior'].append(s3)
        # ft_new_file(name, dic)
        ft_main_cons(dic, names, passwords, name)
    elif int(n) == 3:
        for i in range(len(dic[name]['task'])):
            print(i + 1, dic[name]['task'][i])
        num = int(input('Enter num'))
        for k in dic[name]:
            if k != 'password':
                dic[name][k].pop(int(num - 1))
        print(dic)
        ft_main_cons(dic, names, passwords, name)
    elif int(n) == 4:
        ft_cons(dic, names, passwords)
    else:
        exit()


def ft_cons(dic, names, passwords):
    name, password = ft_console(names, passwords)
    ft_main_cons(dic, names, passwords, name)


def ft_new_file(name, dic):
    try:
        os.remove('./' + name + '.py')
    except:
        name = name
    fd = open('./' + name + '.py', "w")
    for i in range(len(dic[name]['task'])):
        fd.write(dic[name]['date'][i]+','+ dic[name]['task'][i]+','+dic[name]['prior'[i]])


fd = open("./Mock exam/task_source/tasks.txt", "r")
n = int(fd.readline())
dic = {}
names = []
passwords = {}
name = 'p1'
for i in range(n):
    k = fd.readline().split(';')
    dic[k[1]] = {}
    dic[k[1]]['password'] = k[2][0:-1]
    names.append(k[1])
    passwords[names[i]] = k[2][0:-1]
dic = ft_add_work(fd, names, int(fd.readline()), dic)
ft_cons(dic, names, passwords)
print(dic)
fd.close()

