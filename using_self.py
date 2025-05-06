#Assignment:
#Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.




class Student():
   def __init__(self,name,marks):
      self.name=name
      self.marks=marks
 
      
   def display(self):
        print("students detail")
        print(f"student name: {self.name} \nstundent marks: {self.marks}") 
      
    
student1=Student("Ali",65)
print(student1.display())
