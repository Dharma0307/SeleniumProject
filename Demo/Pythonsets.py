my_sets = {"Duster", "Board", "Chalk"}
print(my_sets)

for x in my_sets:
    print(x)

print("Duster" in my_sets) # true

my_sets.add("Pen")
print(my_sets)

my_sets.update(["pencil", "eraser"])
print(my_sets)

print(len(my_sets))

my_sets.remove("pencil")
print(my_sets)
my_sets.discard("eraser")
print(my_sets)

my_sets.pop()
print(my_sets)

del my_sets

my_sets_2 = {"Apples", 1, 2, ("a", "b", "c")}
print(my_sets_2)

my_list = [2, 4, 5]
print(my_list)
my_set_3 = set(my_list)
print(my_set_3)


# union | intersection | difference | symmetric diff |
A = {"a", "b", 1, 2, 3}
B = {"b", "c", 3, 4, 5}

print(A.union(B))
print(A | B)

print(A.intersection(B))
print(A & B)

print(A.difference(B))
print(A - B)

print(A.symmetric_difference(B))
print(A ^ B)

