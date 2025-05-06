#Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.


class Car:
    def __init__(self,brand):
        self.brand_name=brand
   

    def start(self):
        print(f"{self.brand_name} is starting")  


car1=Car("Toyota") 
car2=Car("hyundai") 
car3=Car("suzuki") 

print(car1.brand_name)
car1.start()

print(car2.brand_name)
car2.start()