print("welcome to Python Tutorial")

# case sensitive, underscore, letters(A-Z), NUMBER(0-9)
x = 5
y = "Automation"

print(x)
print(y)

print("Hello " + y)

x = 5
y = 20

print(x+y)

if 10 > 5:
    print("10 is greater than five")

def sum(a , b):
    print(a + b)

x = sum(20, 30)


x = 10
y = 40
z = 4.5

print(type(z))


# casting
x = int(z)
y = int(x)
z = str(y)

print(x)
print(y)
print(z)

x = "Hello world"
print(x[6:11])
print(len(x))
print(x.lower())
print(x.upper())

# strip function
x = "     My Name is Dharma    "
print(x.strip())

# replace

x = " I am indian, a man"
print(x.replace("i", "I"))
print(x.split(","))


# input from user

print("Enter your name:")
x = input()
print("Hello" + x)



