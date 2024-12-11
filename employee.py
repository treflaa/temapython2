class Employee:
    """Clasa de bază comună pentru toți angajații"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        """Afișează numărul de angajați"""
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__(self):
        Employee.empCount -= 1

    def update_salary(self, new_salary):
        self.salary = new_salary

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name] = status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee):
    mgr_count = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = f"F09 {department}"
        Manager.mgr_count += 1
    def display_employee(self, X):
        if X % 3 == 0:
            print("Name: ", self.name)
        elif X % 3 == 1:
            print("Salary: ", self.salary)
        elif X % 3 == 2:
            print("Department: ", self.department)


if __name__ == "__main__":
    X = 5
    Y = 12

    emp1 = Employee("Ion", 3000)
    emp2 = Employee("Maria", 3500)

    mgr1 = Manager("Andrei", 5000, "DevTeam_A")
    mgr2 = Manager("Elena", 5500, "DevTeam_A")
    mgr3 = Manager("Radu", 6000, "DevTeam_A")
    mgr4 = Manager("Mihai", 6200, "DevTeam_A")

    emp1.display_employee()
    emp2.display_employee()
    mgr1.display_employee(X)
    mgr2.display_employee(X)
    mgr3.display_employee(X)
    mgr4.display_employee(X)

    print("\nTotal Employees:")
    emp1.display_emp_count()
    print("Total Managers: ", Manager.mgr_count)
