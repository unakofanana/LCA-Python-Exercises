# Question 1: Using a for loop with a list

fruits = ["apple", "banana", "orange", "grape"]

for fruit in fruits:
    print(fruit)


#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

count = 5

while count >= 1:
    print(count)
    count -= 1


#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

for i in range(1, 11):
    print(i * i)


#-------------------------------------------------------------------------
# Question 4: Using the random module

import random

colors = ["red", "blue", "green", "yellow", "purple"]

for i in range(3):
    print(random.choice(colors))


#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# First create a separate file called: math_operations.py
# (I’ll give you that code below)

import math_operations

# Using functions from the module
print("Add:", math_operations.add(5, 3))
print("Subtract:", math_operations.subtract(5, 3))
print("Multiply:", math_operations.multiply(5, 3))
print("Divide:", math_operations.divide(5, 3))


# Simple calculator using while loop

while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /) or 'q' to quit: ")

    if operation == 'q':
        break

    if operation == '+':
        print("Result:", math_operations.add(num1, num2))
    elif operation == '-':
        print("Result:", math_operations.subtract(num1, num2))
    elif operation == '*':
        print("Result:", math_operations.multiply(num1, num2))
    elif operation == '/':
        print("Result:", math_operations.divide(num1, num2))
    else:
        print("Invalid operation")
    def add(a, b):
     return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"