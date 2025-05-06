#Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position

    def get_employee_info(self):
        return(f"Employee name is: {self.name}  Employee position is : {self.position}")

class Department:
    def __init__(self,department_name,employee):
       self.department_name =department_name 
       self.employee= employee

    def get_department_info(self):
        return f"Department : {self.department_name} , employee : {self.employee.get_employee_info()}"  


employee1= Employee("Ali","software engineer")

department1=Department("IT department", employee1)
print(department1.get_department_info())