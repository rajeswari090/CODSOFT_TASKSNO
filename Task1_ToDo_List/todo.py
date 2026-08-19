tasks = []


def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\n----- TO-DO LIST -----")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


while True:
    print("\n===== TO-DO LIST APPLICATION =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        if task.strip():
            tasks.append(task)
            print("Task added successfully!")
        else:
            print("Task cannot be empty.")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()

        if tasks:
            try:
                number = int(input("Enter task number to update: "))

                if 1 <= number <= len(tasks):
                    new_task = input("Enter the new task: ")

                    if new_task.strip():
                        tasks[number - 1] = new_task
                        print("Task updated successfully!")
                    else:
                        print("Task cannot be empty.")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        show_tasks()

        if tasks:
            try:
                number = int(input("Enter task number to delete: "))

                if 1 <= number <= len(tasks):
                    deleted_task = tasks.pop(number - 1)
                    print(f"Deleted: {deleted_task}")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")
