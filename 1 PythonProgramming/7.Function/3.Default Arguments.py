# Function definition 
def showinfo( name, city = "Hyderabad" ):
   "This prints a passed info into this function"
   print ("Name:", name)
   print ("City:", city)
   return

# Now call showinfo function
showinfo(name = "Ansh", city = "Delhi")
showinfo(name = "Shrey")

# ====================================================================================================

# function definition 
def percent(phy, maths, maxmarks=200):
   val = (phy + maths) * 100/maxmarks
   return val

phy = 60
maths = 70
# function calling with default argument
result = percent(phy, maths)
print ("percentage:", result)

phy = 40
maths = 46
result = percent(phy, maths, 100)
print ("percentage:", result)

# ====================================================================================================

