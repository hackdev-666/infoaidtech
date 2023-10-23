name=input("Enter your name: ")
print("\nTO-DO LIST")
tasks = []
def add():
    t = input("Enter the task: ")
    tasks.append(t)
    print("\nTask is added.")
def view():
    if tasks:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        print("\n")    
    else:
        print("No tasks in the list.\n")
def remove():
    view()
    if tasks:
        try:
            index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)
                print(f"\nTask '{removed_task}' removed.")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Invalid input. Please enter a valid task number.\n")
while True:
    print("1. Press 1 to add a task to your list. \n2. Press 2 to view your list.")
    print("3. Press 3 to delete a task from your list. \n4. Quit\n")
    choice = input("Enter your choice: ")
    if choice == "1":
        add()
    elif choice == "2":
        view()
    elif choice == "3":
        remove()
    elif choice == "4":
        print("\nHave a nice day,",name,"....")
        break
    else:
        print("Invalid choice. Please enter a valid option.\n")
    





 





