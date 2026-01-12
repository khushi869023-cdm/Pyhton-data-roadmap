marks1 = 94.4  #built-in float data type
marks2 = 88.9
marks3 = 76.5
marks4 = 66.0
marks5 = 45.1

marks = [94.4, 88.9, 76.5, 66.0, 45.1]  #list data type

print (marks)   #prints the entire list
print (type(marks))  #prints the data type of variable 'marks'

print (marks[0])  #prints the first element of the list
print (marks[1])  #prints the second element of the list

print (len(marks))  #prints the length of the list

student = ["Khushi", 22, 5.6, True, None]  #list with multiple data types
print (student)  #prints the entire list
print (type(student))  #prints the data type of variable 'student' 

list = [2,5,6,7,8]
list.append(9)   #adds 9 at the end of the list

print (list)  #prints the updated list
print(list.sort())  #sorts the list in ascending order
print (list)  #prints the sorted list

print (list.sort(reverse=True))  #sorts the list in descending order
print (list)  #prints the sorted list

list2 = ['a', 'b', 'f', 'd', 'e']
print (list2.sort(reverse=True))  #sorts the list in descending order
print (list2)  #prints the sorted list

list3 = [1, 2, 3, 4, 5]
list3.reverse()  #reverses the list

list3.index(3)  #finds the index of element 3 in the list
list3.insert(2, 10)  #inserts 10 at index 2 in the list 
print (list3)  #prints the list
list3.remove(4)  #removes element 4 from the list
print (list3)  #prints the updated list
list3.pop()  #removes the last element from the list
print (list3)  #prints the updated list  