employees = []
# update employee
def update_employee():
    emp_id = int(input("Enter ID to update: "))
    for e in employees:
        if e["id"] == emp_id:
            print("1. Department  2. Role  3. Salary")
            ch = input("Enter choice: ")
            if ch == "1":
                e["department"] = input("Enter new Department: ")
            elif ch == "2":
                e["role"] = input("Enter new Role: ")
            elif ch == "3":
                e["salary"] = float(input("Enter new Salary: "))
            print("Updated successfully")
            return
    print("Employee not found")
update_employee()