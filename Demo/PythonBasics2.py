if 5 > 3:
    print("5 is greater than 3")


num = 1
if num > 1:
    print("This is positive number")
elif num == 1:
    print("Num is Zero")
else:
    print("This is negative number")


# for loop
num = [1, 2, 3, 4, 5]
sum= 0
for val in num:
    sum = sum + val
print("Total is ", sum)

fruits = ["apple", "oranges", "grapes"]

for val in fruits:
    print(val)
else:
    print("no fruit")

# while loop
print("Enter the number:")
num = int(input())
sum = 0
i = 1

while i<num:
    sum = sum+i
    i = i+1
print("total sum", sum)
