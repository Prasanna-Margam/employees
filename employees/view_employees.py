employees = []
# view employee
def view_employees():
    if not employees:
        print("No employees found")
    else:
        for e in employees:
            print(e)
view_employees()