employees = []
# delete employee
def delete_employee():
    emp_id = int(input("Enter ID to delete: "))
    for e in employees:
        if e["id"] == emp_id:
            employees.remove(e)
            print("Deleted successfully")
            return
    print("Employee not found")
delete_employee()
