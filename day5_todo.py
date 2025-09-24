while True:
    print("\n==== To-Do List ====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("View tasks here...")
    elif choice == "2":
        print("Add task here...")
    elif choice == "3":
        print("Mark task here...")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
