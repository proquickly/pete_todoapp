import pete_todoapp.lib


def main():
    todo_lists = {}
    todo_list = input("List name?: ")
    todo_lists[todo_list] = pete_todoapp.lib.ToDoList(todo_list)
    while True:
        task = input("Task name?: ")
        task_description = input("Task description?: ")
        task_due_date = input("Task due date?: ")
        if task == "q":
            break
        todo_lists[todo_list].tasks.append(
            pete_todoapp.lib.Task(task, task_description, task_due_date))
    todo_lists[todo_list].show_tasks()


if __name__ == "__main__":
    main()
