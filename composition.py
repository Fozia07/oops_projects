#Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def __init__ (self,engine_type):
        self.engine_type=engine_type
 
    def start(self):
       return (f'The {self.engine_type} engine is starting')
  #composition Car class  
class Car:
   def __init__(self,brand,engine):
      self.brand=brand
      self.engine=engine

   def start_car(self):
     print(f"{self.brand} car is start. {self.engine.start()}")

engine=Engine("v8")
car=Car("Toyota",engine)   

print(car.start_car())