class Employee:
    company_name = "TechCorp"  # Class attribute (shared by all)
    employee_count = 0         # Class attribute
    
    def __init__(self, name, salary):
        self.name = name       # Instance attribute (unique to each)
        self.salary = salary   # Instance attribute
        Employee.employee_count += 1

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

# Class attributes are the same for all instances
print(emp1.company_name)  # TechCorp
print(emp2.company_name)  # TechCorp
print(Employee.company_name)  # TechCorp

# Instance attributes are different
print(emp1.name)  # Alice
print(emp2.name)  # Bob

print(Employee.employee_count)  # 2