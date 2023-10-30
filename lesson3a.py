#LIST COUT..
#CREATE A LIST OF 6 APPS

apps = ["netflix", "whatsapp", "instagram", "facebook", "twitter"]
#indexing : item on the list is given an index(start from 0)
#ordered

print(apps[2])
print(apps[4])


#list operations 
#add a new item ..append()

apps.append("tiktok")
print(apps)

#replace an item in the list

apps[1] = "whatsappgb"
print(apps)


#range in list (:)
#first index is included
#last index is excluded
#whatsapp -1
#instagram -2

print(apps[1:3])

print(apps[1:5])