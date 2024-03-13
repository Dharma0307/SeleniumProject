my_dict = {
    "class": "Animal",
    "name": "Lion",
    "age": "32"
}
print(my_dict)
print(my_dict["name"])
print(my_dict.get("name"))
print(my_dict.values())

for x in my_dict:
    print(x) # it will print all keys as output
    print(my_dict[x]) # it will print values


for x , y in my_dict.items():
    print(x, y)

my_dict["name"]= "Tiger"
print(my_dict)

my_dict["color"] = "Blue"
print(my_dict)

my_dict.pop("color")
print(my_dict)

my_dict.popitem()
print(my_dict)

my_dict.clear()
print(my_dict)
