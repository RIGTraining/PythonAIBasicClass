class User:
    user = input("Enter Username:")

massage = "Welcome"
login = User()
print(massage,login.user)

# ====================================================================================================
# The __str__() Function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)
print(p1)

# ====================================================================================================
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#output: Hello my name is John

# ====================================================================================================
#The self Parameter


