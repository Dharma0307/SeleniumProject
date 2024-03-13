my_tuple = ("Apples", "Oranges", "Grapes")

print(my_tuple)
print(my_tuple[1])
print(my_tuple[-1])
print(my_tuple[0:2])

for val in my_tuple:
    print(val)

print(len(my_tuple))

my_tuple_2 = ("Apple", (1, 2, 3), ["Delhi", "Bangalore"])
print(my_tuple_2)
print(my_tuple_2[2][1])

my_tuple_2[2][1] = "Hyderabad"
print(my_tuple_2)

print("Apple" in my_tuple_2) # true
print("Banana" in my_tuple_2) # false
