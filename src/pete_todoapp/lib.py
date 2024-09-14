class ToDoList:
    def __init__(self, list_name):
        self.list_name = list_name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        print("Name, Description, Due Date")
        for task in self.tasks:
            print(task)


class Task:
    def __init__(self, name, description, due_date):
        self.name = name
        self.description = description
        self.due_date = due_date

    def __str__(self):
        return f"{self.name}: {self.description} due: {self.due_date}"
