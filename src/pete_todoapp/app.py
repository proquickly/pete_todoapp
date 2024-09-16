from lib import Task, ToDoList


def main():
    todo_lists = {}
    todo_list = input("List name?: ")
    todo_lists[todo_list] = ToDoList(todo_list)
    while True:
        task = input("Task name?: ")
        task_description = input("Task description?: ")
        task_due_date = input("Task due date?: ")
        if task == "q":
            break
        todo_lists[todo_list].tasks.append(
            Task(task, task_description, task_due_date))
    todo_lists[todo_list].show_tasks()


if __name__ == "__main__":
    main()
