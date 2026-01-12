#Print function
print ("hello world !\t Welcome to Python programming.")

#Variables 
name = "Khushi"
age = 22
print (name, age)

#data types
name = "Khushi"   #string
age = 22          #integer(+ve/-ve whole numbers)
height = 5.6     #float (decimal numbers)
is_student = True  #boolean (True/False)    
none = None      #NoneType (represents absence of value)

print (type(name))  #prints the data type of variable 'name'
print (type(age))   #prints the data type of variable 'age'

#keywords
import keyword
print (keyword.kwlist)  #prints all the keywords in python

#print sum
a=455
b=345
print("The sum of a and b is:", a+b)

#Input function
name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to Python programming.")

#operators
x = 10
y = 5
print("Addition:", x + y)
print("Subtraction:", x - y)

#Type Conversion
print("String to Integer:", int("123") + 10)


a="100"
b=200
print("String to Integer:", int(a) + b)