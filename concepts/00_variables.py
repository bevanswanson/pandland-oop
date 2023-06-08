################### Variable Assignment ################
x = 10
name = "John"
is_valid = True

################ Dynamic Typing ################
x = 10
print(x)  # Output: 10
x = "Hello"
print(x)  # Output: Hello

################ Case Sensitive ################

myVariable = 10
myvariable = 20

################ Variable Scope ################
def my_function():
    local_variable = 10  # Local variable
    print(local_variable)


my_function()  # Output: 10

global_variable = 20  # Global variable


def another_function():
    print(global_variable)


another_function()  # Output: 20

################ Variable Unpacking ################
x, y, z = 1, 2, 3
print(x, y, z)  # Output: 1 2 3

################ Variable Interpolation ################

name = "Iman"
age = 25

# f-strings
print(f"My name is {name} and I'm {age} years old.")

# str.format()
print("My name is {} and I'm {} years old.".format(name, age))

# %-formatting
print("My name is %s and I'm %d years old." % (name, age))
