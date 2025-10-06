employees = []
def menu():
    while True:
        print("\n===== Employee menu =====")
        print("\n 1.Add \n 2.View \n 3.Search\n 4.Update\n 5.Delete \n 6.Exit")
        ch = input("Enter choice: ")
        if ch == "1":
            add_employee(employees)
        elif ch == "2":
            view_employees(employees)
        elif ch == "3":
            search_employee(employees)
        elif ch == "4":
            update_employee(employees)
        elif ch == "5":
            delete_employee(employees)
        elif ch == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

menu()