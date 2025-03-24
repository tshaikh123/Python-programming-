
tasks=[]

print("\nTask List Manager")
print("1. Add Task")
print("2. Remove Task")
print("3. Update Task")
print("4. Display Tasks")
print("5. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    task = input("Enter task to add: ")
    tasks.append(task)
    print(f'Task "{task}" added successfully!')

elif choice == "2":
    task = input("Enter task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print(f'Task "{task}" removed successfully!')
    else:
        print(f'Task "{task}" not found!')

elif choice == "3":
    old_task = input("Enter the task to update: ")
    if old_task in tasks:
        new_task = input("Enter the new task: ")
        tasks[tasks.index(old_task)] = new_task
        print(f'Task updated successfully!')
    else:
        print(f'Task "{old_task}" not found!')

elif choice == "4":
    if tasks:
        print("Task List:")
        for task in tasks:
            print(f"• {task}")
    else:
        print("No tasks available!")

elif choice == "5":
    print("Exiting Task Manager. Goodbye!")

else:
    print("Invalid choice! Please enter a valid option.")