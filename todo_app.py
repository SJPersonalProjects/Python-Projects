# To-Do App: Add/remove tasks from a list using menu options.

# An empty list.
todo_list = []


while True:
    print("\nTo-Do App. Write options below:_")
    print("Add task")
    print("Remove task")
    print("Check task")
    print("Q to quit")
    task = input("\nI choose: ")

    if task.lower() == 'add task':
        add_task = input("Add task: ")
        if add_task not in todo_list:
            todo_list.append(add_task)
            print("Task added successfully.")

    elif task.lower() == 'remove task':
        remove_task = input("Remove task: ")
        if remove_task in todo_list:
            todo_list.remove(remove_task)

    elif task.lower() == 'check task':
        print(todo_list)
    elif task.lower() == 'q':
        break
