import art

employees = ["Rahman", "Sophia", "Liam", "John"]

def add_fruits_from_input(user_input):
    employee1, employee2, employee3 = user_input.split(",")
    employee1, employee2, employee3 = employee1.strip(), employee2.strip(), employee3.strip()

    employees.extend([employee1, employee2, employee3])

def show_employees_list():
    print("Employee List:")
    for i, employee in enumerate(employees, start=1):
        print(f"{i}. {employee}")

def unpacking_employees_list():
    first_employee, second_employee, *other_employees = employees
    print("Unpacking the list of employees:")
    print(f"- First employee: {first_employee}")
    print(f"- Second employee: {second_employee}")
    print(f"- Other employees: {other_employees}")


def main():
    while True:
        print(art.employees_app)

        user_input = input("Enter the names of three new employees (separated by commas): ").title()
        add_fruits_from_input(user_input)
        show_employees_list()
        unpacking_employees_list()

        close_app = input("Do you want to add more? type 'yes' or 'no': ")
        if close_app != "yes":
            break

main()



