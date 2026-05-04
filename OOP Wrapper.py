class Employee:
    def __init__(self, name, age, employee_id=None, salary=None):
        
        self.name = name
        self.age = age
        
        self.__employee_id = employee_id
        self.__salary = salary

   
    def get_employee_id(self):
        return self.__employee_id


    def set_employee_id(self, emp_id):
        self.__employee_id = emp_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be positive.")

    def display(self):
        print(f"ID: {self.__employee_id} | Name: {self.name} | Age: {self.age} | Salary: {self.__salary}")

    def __del__(self):
        
        print(f"Cleanup: Employee {self.name} record removed from memory.")


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        
        super().__init__(name, age, employee_id, salary)
        self.department = department

  
    def display(self):
        print(f"[Manager] Dept: {self.department}", end=" | ")
        super().display()


class Developer(Employee):
    def __init__(self, name, age, employee_id, salary, language):
        super().__init__(name, age, employee_id, salary)
        self.language = language


    def display(self):
        print(f"[Developer] Language: {self.language}", end=" | ")
        super().display()


def main_menu():
    employees = []
    
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Manager")
        print("2. Add Developer")
        print("3. Display All Employees")
        print("4. Check Class Relationship (issubclass)")
        print("5. Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Name: ")
            age = int(input("Age: "))
            eid = input("ID: ")
            sal = float(input("Salary: "))
            dept = input("Department: ")
            employees.append(Manager(name, age, eid, sal, dept))

        elif choice == '2':
            name = input("Name: ")
            age = int(input("Age: "))
            eid = input("ID: ")
            sal = float(input("Salary: "))
            lang = input("Programming Language: ")
            employees.append(Developer(name, age, eid, sal, lang))

        elif choice == '3':
            print("\n--- Employee List ---")
            for emp in employees:
                emp.display()

        elif choice == '4':
            print(f"Is Manager a subclass of Employee? {issubclass(Manager, Employee)}")
            print(f"Is Developer a subclass of Employee? {issubclass(Developer, Employee)}")

        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main_menu()
