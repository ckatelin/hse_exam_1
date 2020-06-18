# The main program code goes here

from utils import input_number, input_value_from_list, input_datetime, get_hash

USR_NAME = 0
USR_LOGIN = 1
USR_PASS = 2
USR_TASKS = 3

TASK_DATETIME = 0
TASK_NAME = 1
TASK_PRIORITY = 2
TASK_USER = 3

MIN_ACTION = 1
MAX_ACTION = 4

TASK_ALL_USERS = 'all'

FILE_NAME = 'tasks.txt'
PRIORITIES = ["Low", "Medium", "High"]


def add_task_to_users(users, task):
    for login in users:
        users[login][USR_TASKS].append(task)


def read_data(file_name):
    # The users dictionary: key = username,
    # value = user object (list of values)
    users = {}
    tasks = []
    with open(file_name, 'r') as f:
        num_users = int(f.readline())
        i = 0
        while i < num_users:
            line = f.readline().strip()
            user = line.split(';')
            # When reading a user, we allocate a list for storing
            # his/her tasks
            user.append([])            
            users[user[USR_LOGIN]] = user
            i += 1
        num_tasks = int(f.readline())
        i = 0
        while i < num_tasks:
            line = f.readline().strip()
            task = line.split(';')
            tasks.append(task)            
            if task[3] == TASK_ALL_USERS:
                add_task_to_users(users, task)
            else:
                users[task[TASK_USER]][USR_TASKS].append(task)
            i += 1
        for login in users:
            users[login][USR_TASKS].sort()
    return (users, tasks)


def save_data(users, tasks, file_name):
    with open(file_name, 'w') as f:
        f.write(f'{len(users)}\n')
        for user in users.values():
            f.write(f'{user[USR_NAME]};{user[USR_LOGIN]};{user[USR_PASS]}\n')
        f.write(f'{len(tasks)}\n')
        for task in tasks:
            f.write(';'.join(task))
            f.write('\n')


def list_tasks(user):
    print(f'{"Date and time":<20}{"Name":<30}{"Priority":<6}')
    for task in user[USR_TASKS]:
        print(f'{task[TASK_DATETIME]:<20}{task[TASK_NAME]:<30}{task[TASK_PRIORITY]:<6}')


def input_new_task():
    name = input("Enter task name: ")
    dt = input_datetime("Enter date and time: ")
    priority = input_value_from_list("Enter task priority (Low/Medium/High): ", PRIORITIES)
    all_users = input("Do you want to create this task for all users? (Y/N): ")

    task = [dt, name, priority, '']
    if all_users.lower() == 'y':
        task[TASK_USER] = TASK_ALL_USERS
    # An empty string will be replaced by the current user's login in the main program
    return task


def delete_task(users, tasks, task):
    # Remove from the tasks list
    tasks.remove(task)
    # Remove from lists of tasks related to users
    # Errors may arise if a value is not in the list, hence the try-except block
    for user in users.values():
        try:
            user[USR_TASKS].remove(task)
        except:
            pass


users, tasks = read_data(FILE_NAME)

while True:
    login = input("Enter username: ")
    if login == "":
        break
    password = input("Enter password: ")
    if login not in users or users[login][USR_PASS] != get_hash(password):
        print("Incorrect username/password")
        continue
    user = users[login]

    while True:
        print("1 - list all tasks")
        print("2 - add new task")
        print("3 - delete task")
        print("4 - logout")
        action = input_number("Select an action: ", MIN_ACTION, MAX_ACTION)
        if action == 1:
            list_tasks(user)
        elif action == 3:
            print("Your tasks: ")    
            i = 1
            for task in user[USR_TASKS]:
                print(f'{i}: {task[TASK_NAME]}')
                i += 1
            to_delete_index = input_number("Select a task to delete: ", 1, len(user[USR_TASKS]) + 1)
            delete_task(users, tasks, user[USR_TASKS][to_delete_index - 1])
            save_data(users, tasks, FILE_NAME)
        elif action == 2:
            new_task = input_new_task()
            if new_task:
                if new_task[TASK_USER] == TASK_ALL_USERS:
                    add_task_to_users(users, new_task)
                else:
                    # Only current user
                    new_task[TASK_USER] = user[USR_LOGIN]
                    user[USR_TASKS].append(new_task)
                for u in users.values():
                    u[USR_TASKS].sort()
                tasks.append(new_task)
                save_data(users, tasks, FILE_NAME)
                print("Task added successfully")

        elif action == 4:
            break
