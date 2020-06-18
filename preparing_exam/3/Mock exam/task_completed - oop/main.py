from utils import input_number, input_value_from_list, input_datetime, get_hash
from classes import User, Task

MIN_ACTION = 1
MAX_ACTION = 4

ACTION_LIST_TASKS = 1
ACTION_NEW_TASK = 2
ACTION_DELETE_TASK = 3
ACTION_EXIT = 4

TASK_ALL_USERS = 'all'

FILE_NAME = 'tasks.txt'
PRIORITIES = ["Low", "Medium", "High"]


def add_task_to_users(users, task):
    for login in users:
        users[login].add_task(task)


def read_data(file_name):
    # The users dictionary: key = username,
    # value = user object
    users = {}
    tasks = []
    with open(file_name, 'r') as f:
        num_users = int(f.readline())
        i = 0
        while i < num_users:
            line = f.readline().strip()
            parts = line.split(';')
            user = User(parts[0], parts[1], parts[2])
            users[user.login] = user
            i += 1
        num_tasks = int(f.readline())
        i = 0
        while i < num_tasks:
            line = f.readline().strip()
            parts = line.split(';')
            task = Task(parts[0], parts[1], parts[2], parts[3])
            if parts[3] == TASK_ALL_USERS:
                add_task_to_users(users, task)
            else:
                user = users.get(parts[3], None)
                if user:
                    user.add_task(task)
            tasks.append(task)
            i += 1
    return (users, tasks)


def save_data(users, tasks, file_name):
    with open(file_name, 'w') as f:
        f.write(f'{len(users)}\n')
        for user in users.values():
            f.write(f'{user.name};{user.login};{user.password}\n')
        f.write(f'{len(tasks)}\n')
        for task in tasks:
            f.write(f'{task.deadline};{task.name};{task.priority};{task.user_ref}\n')


def list_tasks(user):
    print(f'{"Date and time":<20}{"Name":<30}{"Priority":<6}')
    for task in user.tasks:
        print(f'{task.deadline:<20}{task.name:<30}{task.priority:<6}')


def input_new_task(user_login):
    name = input("Enter task name: ")
    dt = input_datetime("Enter date and time: ")
    priority = input_value_from_list("Enter task priority (Low/Medium/High): ", PRIORITIES)
    all_users = input("Do you want to create this task for all users? (Y/N): ")

    if all_users.lower() == 'y':
        return Task(dt, name, priority, TASK_ALL_USERS)
    else:
        return Task(dt, name, priority, user_login)


def delete_task(users, tasks, task):
    # Remove from the tasks list
    tasks.remove(task)
    # Remove from lists of tasks related to users
    # Errors may arise if a value is not in the list, hence the try-except block
    for user in users.values():
        try:
            user.remove_task(task)
        except:
            pass


users, tasks = read_data(FILE_NAME)

while True:
    login = input("Enter username: ")
    if login == "":
        break
    password = input("Enter password: ")
    if login not in users or users[login].password != get_hash(password):
        print("Incorrect username/password")
        continue
    user = users[login]

    while True:
        print("1 - list all tasks")
        print("2 - add new task")
        print("3 - delete task")
        print("4 - logout")
        action = input_number("Select an action: ", MIN_ACTION, MAX_ACTION)
        if action == ACTION_LIST_TASKS:
            list_tasks(user)
        elif action == ACTION_DELETE_TASK:
            print("Your tasks: ")    
            i = 1
            for task in user.tasks:
                print(f'{i}: {task.name}')
                i += 1
            to_delete_index = input_number("Select a task to delete: ", 1, len(user.tasks) + 1)
            delete_task(users, tasks, user.tasks[to_delete_index - 1])
            save_data(users, tasks, FILE_NAME)
        elif action == ACTION_NEW_TASK:
            new_task = input_new_task(user.login)

            if new_task.user_ref == TASK_ALL_USERS:
                add_task_to_users(users, new_task)
            else:
                # Only current user
                user.add_task(new_task)

            tasks.append(new_task)
            save_data(users, tasks, FILE_NAME)
            print("Task added successfully")

        elif action == ACTION_EXIT:
            break
