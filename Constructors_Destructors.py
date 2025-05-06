#Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("object is created") 

    def __del__(self):
        print ("object is disturcted")        


#object is created
logger1 = Logger()

#object is del
del logger1