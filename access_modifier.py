#Create a class Employee with:
#a public variable name,
#a protected variable _salary, and
#a private variable __ssn.
#Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self):
        self.employee_name = "Ali"
        self._salary = 65000
        self.__ssn = "123_456_789"


employee1=Employee()  
#public variable
print(employee1.employee_name)
#protected variable
print(employee1._salary)
#private variabale

try:
    print("ssn: ",{employee1.__ssn})
except AttributeError as e:

  print (f"Error: {e}")

#accesssing the private variable via name mangling
print(f"ssn (via name mangling): {employee1._Employee__ssn}")  

