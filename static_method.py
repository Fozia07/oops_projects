#Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConvertor:
    @staticmethod
   
    def celsius_to_fahrenheit(tem):
      return (tem * 9/7)+32
    

temp1=TemperatureConvertor()
celsius=32
fahrenheit=temp1.celsius_to_fahrenheit(celsius)
print(f"{celsius} celsius is equal to  {fahrenheit} fahrenheit")
