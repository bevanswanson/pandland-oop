################### Conditional Statements ################

# if statement
x = 10
if x > 0:
    print("x is positive")

# if-else statement
x = -5
if x > 0:
    print("x is positive")
else:
    print("x is non-positive")

# if-elif-else statement
x = 0
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

################### Looping Statements ################

# for loop
months = ["January", "February", "March"]
for month in months:
    print(month)

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# break statement
for i in range(10):
    if i == 5:
        break
    print(i)

# continue statement
for i in range(10):
    if i == 5:
        continue
    print(i)

################### Exception Handling ################

# try-except statement
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")

# finally statement
try:
    x = 10 / 0
    x = x + 10
except ZeroDivisionError:
    print("Error: Division by zero")
finally:
    print("Finally block executed")


# raise statement
def sqrt(x):
    if x < 0:
        raise ValueError("Input must be a non-negative number")
    else:
        return x**0.5


print(sqrt(4))  # Output: 2
print(sqrt(-4))  # Raises ValueError


################### Comprehensions ################

# List comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Dictionary comprehension
months = ["January", "February", "March"]
month_lengths = {mothn: len(mothn) for mothn in months}
print(month_lengths)  # Output:{'January': 7, 'February': 8, 'March': 5}

# Set comprehension
numbers = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
unique_numbers = {x for x in numbers}
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}
