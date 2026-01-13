tup= (2 , 1 , 3 , 4 , 5)  #tuple data type  
print (type(tup))  #prints the data type of variable 'tup'  
print (tup[4])  #prints the tuple 'tup'

tup2 = ()  #empty tuple
print (type(tup2))  #prints the data type of variable 'tup2'

tup3 = (1)  #single element tuple
print (type(tup3))  #prints the data type of variable 'tup3'
            #int 
tup4 = (1,)  #single element tuple with comma
print (type(tup4))  #prints the data type of variable 'tup4
            #tuple

tup5 = (1, 2.5, "Hello", True)  #tuple with different data types
print (tup5)  #prints the tuple 'tup5'
print (tup5[0:2])  #prints elements from index 0 to 1

#Tuples are immutable (cannot be changed)
#tup5[1] = 3.5  #This will raise an error
#print (tup5)  #prints the tuple 'tup5'

print (tup.index(3))  #prints the index of element '3' in tuple 'tup'