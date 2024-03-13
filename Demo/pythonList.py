mylist = ["Tokoya", "london", "newyork", "singapore"]
print(mylist)
print(mylist[2])

mylist[2] = "new Delhi"
print(mylist)

for val in mylist:
    print(val)

print(len(mylist))

mylist.append("Botson")
print(mylist)
mylist.insert(3, "India")
mylist.remove("India")
print(mylist)
mylist.pop()
print(mylist)
del mylist[2]
print(mylist)

mylist.clear()
print(mylist)

my_list_fruits = ["oranges", "grapes", "Apple"]
my_list_fruits.reverse()
print(my_list_fruits)

my_list_1 = ["apple", 1, 2, 3,]
my_list_2 = ["apple", [1, 2, 3], ["a", "b", "c"]]
print(my_list_1)
print(my_list_2)
print(my_list_2[1][1])
