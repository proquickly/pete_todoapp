from lib import Task, ToDoList


def main():
    """
    Manages multiple to-do lists in an interactive console session.

    The user can create to-do lists, add tasks with descriptions and due dates, and display tasks.
    The session continues until the task name entered is 'q'.
    """

    todo_lists = {}

    while True:
        print("Current To-Do Lists:")
        for list_name in todo_lists:
            print(list_name)

        todo_list = input("Enter the name of the to-do list you want to use or create: ")
        if todo_list not in todo_lists:
            todo_lists[todo_list] = ToDoList(todo_list)

        task = input("Enter the task name (enter 'q' to quit): ")
        if task.lower() == "q":
            break

        task_description = input("Enter the task description: ")
        task_due_date = input("Enter the task due date: ")

        todo_lists[todo_list].tasks.append(
            Task(task, task_description, task_due_date))

    for list_name, todo_list in todo_lists.items():
        print(f"List: {list_name}")
        todo_list.show_tasks()


if __name__ == "__main__":
    main()