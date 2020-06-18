class User:
    def __init__(self, name, login, password):
        self.password = password
        self.login = login
        self.name = name
        self.tasks = []

    def add_task(self, task):
        # A more optimal solution would be inserting at the correct index
        # straightaway
        self.tasks.append(task)
        self.tasks.sort(key=lambda t: t.deadline)

    def remove_task(self, task):
        self.tasks.remove(task)


class Task:
    def __init__(self, deadline, name, priority, user_ref):
        self.priority = priority
        self.name = name
        self.deadline = deadline
        self.user_ref = user_ref