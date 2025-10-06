employees = []
# add employee
def add_employee():
    if len(employees) >= 8:
        print("cannot add employees")
        return
    emp_id = int(input("Enter ID: "))
    for e in employees:
        if e["id"] == emp_id:
            print("ID already exists")
            return
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    role = input("Enter Role: ")
    salary = float(input("Enter Salary: "))
    emp = {"id": emp_id, "name": name, "department": dept, "role": role, "salary": salary}
    employees.append(emp)
    print("Employee added")
add_employee()