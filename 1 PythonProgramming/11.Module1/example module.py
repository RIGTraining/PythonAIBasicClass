import math
print ("Square root of 100:", math.sqrt(100))

# ====================================================================================================

# create mymodule.py
def SayHello(name):
   print ("Hi {}! How are you?".format(name))
   return

def sum(x,y):
   return x+y

def average(x,y):
   return (x+y)/2

def power(x,y):
   return x**y



# create mymodule1.py
import mymodule
mymodule.SayHello("Harish")

import mymodule
print ("sum:",mymodule.sum(10,20))
print ("average:",mymodule.average(10,20))
print ("power:",mymodule.power(10, 2))