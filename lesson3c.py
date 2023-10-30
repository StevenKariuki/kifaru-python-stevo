#DICTIONARIES
#list:ordered,allow duplicates ,changaeble,syntax:()
#tuple:ordered,allow duplicates ,unchangeable,syntax ()


#DICTIONARIES:collections types:unordered,no duplicates ,changeable:sysntax:()  braces 
#JSON:Javascript object notation(API):resemble python dictionaries

#stores data in form of key,value  pairs,,e,g name:"steven"

#design a person:properties->value
person = {
  "name": "Steven",
  "height": 1.8,
  "origin": "Africa",
  "place_of_birth": "Makueni",  "siblings":["johnsom", "ann"]
}
print(type(person))
print(person)


#access items on a dictionary,we use the key to access a value
print(person["height"])

counties = ["Nairobi", "thika", "nakuru"]
print(counties[1])

#access origin
print(person["origin"])

print(person["siblings"][1])
