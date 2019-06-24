#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        print(self.name.title() + " rolled over!")


# In[8]:


my_dog = Dog('Timmy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")


# In[ ]:


my_dog.sit()
my_dog.roll_over()


# In[18]:


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        self.odometer_reading = mileage
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    def fill_gas_tank(self):
        self.gas_tank += kg
    

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# In[19]:


my_new_car.update_odometer(24)
my_new_car.read_odometer()


# In[20]:


def increment_odometer(self, miles):
    self.odometer_reading += miles

    my_used_car = Car('subaru', 'outback', 2013)
    print(my_used_car.get_descriptive_name())
    my_used_car.update_odometer(23500)
    my_used_car.read_odometer()

    my_used_car.increment_odometer(100)
    my_used_car.read_odometer()


# # Inheritance
# 

# In[21]:


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
 

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
    
    


# # Defining Attributes and Methods for the Child Class

# In[ ]:





# In[22]:


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
        
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
        
my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
print(my_tesla.describe_battery())


# # Overriding Methods from the Parent Class

# In[30]:


class ElectricCar(Car):
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")
your_tesla = ElectricCar("Honda", 2019 , 899)
print(your_tesla.fill_gas_tank())


# # Instances as Attributes

# In[32]:


class Battery():
    def __init__(self,amperes,cycles,manufacturer, battery_size=70):
        self.battery_size = battery_size
        self.manufacturer=manufacturer
        self.cycles=cycles
        self.amperes=amperes
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.") 


# In[33]:


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery("abc","2500","200amp",50)
        
        
my_tesla = ElectricCar('tesla','model s',2016)

print(my_tesla.get_descriptive_name())
print(my_tesla.battery.describe_battery())


# In[ ]:





# In[ ]:




