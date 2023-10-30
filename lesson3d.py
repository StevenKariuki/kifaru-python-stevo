#movie data store

godsMustBeCarzy ={
    "characters":["xixo", "Mqudi"],
    "directors": "Billy Chan",
    "location": "Southern Africa",
    "bFilm": 12000,
    "bCharacters": 40000,
    "releaseyear": 2000
}
#access budget for film
print(godsMustBeCarzy["bFilm"])
print(godsMustBeCarzy["bCharacters"])

print(godsMustBeCarzy["bFilm"] + godsMustBeCarzy["bCharacters"])

total =godsMustBeCarzy["bFilm"] +  godsMustBeCarzy["bCharacters"]
print("total budget is", total)

#modify items on a 
godsMustBeCarzy["releaseyear"] = 2002
print(godsMustBeCarzy)

#adding a new item to the dictionary
godsMustBeCarzy["viewers"] = "1B views"
print(godsMustBeCarzy)

#show no duplicates allowed 
godsMustBeCarzy["director"] = "kelly yhu"
print(godsMustBeCarzy)