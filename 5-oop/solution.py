class Car :
     total_car = 0
     def __init__(self,brand,model):   #init means constructor in python.
      self.__brand = brand  #Make the brand variable private.
      self.model = model
      Car.total_car += 1


     def full_name(self) :  #self is like context --> equivalent to this keyword
      return f"{self.__brand} {self.model}"
     

     def get_brand(self):
       return self.__brand + "!"
     @staticmethod
     def general_desc():
       return "Car ---->>>>>"
     

class ElectricCar(Car) :
  def __init__(self,brand,model,battery):
    super().__init__(brand,model)
    self.battery = battery



tesla = ElectricCar("Tesla","Model S","860kWh")
# print(tesla.battery)
# print(tesla.full_name())
      
# my_car = Car("Tesla","A1")
# print(my_car.model)
# print(my_car.full_name())

print(tesla.get_brand())
print(Car.total_car)
print(Car.general_desc())

#55