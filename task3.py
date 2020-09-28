#! python3 

# Have the user enter a number. 
# Use an if...elif statement to determine if the number is 
# a) larger than 1000 
# b) larger than 100 
# c) larger than 10 
# d) larger than 0 
# Output must match one of the valid output statements listed
# (2 points)

# Inputs:
# a number

# Output is a single number that represents a range of numbers:
# "3" : The number is equal to 1000 or is larger than 1000
# "2" : The number is 100 or a number up to 1000 
# "1" : The number is 10 or a number up to 100 
# "0" : The number is 0 or a number up to 10 

print("Enter a number")
a = input()
a = float(a)
b = 1000
c = 100
d = 10
if a >= 1000:
    print("3")
elif a >= 100 < b:
    print("2")
elif a >=10 < c:
    print("1")
elif a >=0 < d:
    print("0")
