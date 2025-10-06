employees = []
# search employee
def search_employee():
    if not employees:
        print("No employees found")
        return
    ch = input("Search by id or name? ")
    if ch == "id":
        emp_id = int(input("Enter ID: "))
        for e in employees:
            if e["id"] == emp_id:
                print(e)
                return
    elif ch == "name":
        name = input("Enter Name: ")
        for e in employees:
            if e["name"].lower() == name.lower():
                print(e)
                return
    print("Employee not found")
search_employee()