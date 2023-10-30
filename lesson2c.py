#DATA TYPES 
#strings, integer ,floats, booleans ,arrays (list,tuple,dictionaries)


#arrays:store a collection of values on the same variables 

student1= "Stevo"
student2= "Mike"
student3= "Sharon"

#LISTS: array collection type where items ordered allow duplicates :modifiable/changeble/mutable
#Syntax:[] Squre brackets
#each item must be separeted by a comma
#Homogenous 
lab5 = ["James", "Chris", "Steven"]
marks = [80,90,100,1090,2]
#heterogenous:stores diff types together
studentsinfo = ["Nancy",100.00,2004,"Stevo", 99.00,2004]
customers = ["Derrick",254700567453,"derrick@gmail.com", "jenny", [25476877629,"jeeniiheon2gmaial.com"] ]

#list operations
#1.display all list items



#2.Access items on a list
#indexing []
#Starts from 0


fruits = ["oranges", "banana", "pinnapple", "mango", "apple"]
print(fruits[3])

#add a new item in the list
#append("item")
fruits.append("beetroot")
print(fruits)
 
 #appending a collection

newlist =["grapes","avocodo"]
fruits.extend(newlist)
print(fruits)

#replace a item on a list
fruits[2]="grapes"
print(fruits)

#deleting items from a list
#1.pop():removes the last item
fruits.pop()
print(fruits)

fruits[4]="snake"
print(fruits)