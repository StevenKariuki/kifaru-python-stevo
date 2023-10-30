#list:ordered,duplicates,mutable/changeable[]
#tuples:ordered,duplicates,immutabable/unchangeable{}
#dictionaries:unordered,no duplicates,changeable{}
#"key":"value" pairs comma separated 

student = {
    "name": "mercy", 
    "age": 25,
    "course": "machine learning",
    "height":1.6,
    "subject":["Vectors", "statistics", "python", "matrix"]
}

#accessing items item:we use key to access value
 
print(student["course"])
print(student["subject"][2])

#add a new item

student["grade"] = "A"
print(student)


#modify/change
student["age"] = 26
print(student)