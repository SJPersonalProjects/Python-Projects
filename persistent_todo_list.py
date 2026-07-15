# Persistent todo list.
# Store tasks permanently using the shelve module.

import shelve

# Open or create the shelf file.
todo_file = shelve.open("todo_list")

# Create an empty task list if it doesn't exist.
if "tasks" not in todo_file:
    todo_file["tasks"] = []

while True:
    print("\n=== To-Do List ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        tasks = todo_file["tasks"]

        if tasks:
            print("\nYour Tasks: ")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("\nNO tasks found.")

    elif choice == '2':
        
        task = input("Enter a new task: ")

        tasks = todo_file["tasks"]
        tasks.append(task)

        # Save the updated list back to the shelf
        todo_file["tasks"] = tasks

        print("Task added successfully.")

    elif choice == '3':
        break

    else :
        print("Invalid choice. Try again.")

# Close the shelf file.
todo_file.close()

print("Goodbye.")