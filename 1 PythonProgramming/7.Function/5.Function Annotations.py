# Function Annotations

def myfunction(a: int, b: int):
   c = a+b
   return c
   
print (myfunction(10,20))
print (myfunction("Hello ", "Python"))

# ====================================================================================================

def total(x : 'marks in Physics', y: 'marks in chemistry'):
   return x+y
print(total(86, 88))
print(total.__annotations__)


# ====================================================================================================

