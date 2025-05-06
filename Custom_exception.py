#Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
    def __init__ (self, massage="age must 18 or older"):
        self.massage =massage
        super(). __init__ (self.massage)

def check_age (age):
    if age < 18:
       raise InvalidAgeError (f"Invalid age {age} you must be at the age age 18 or older")
    else:
        print(f"Age {age} is valid!")

try:
   age =int(input("Enter your age : "))   
   check_age(age)             

except InvalidAgeError as e:
    print(f"Error :{e}")
except ValueError:
    print("please enter a valid integer for age")
    
        