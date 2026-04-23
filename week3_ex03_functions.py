# Question 1: Basic Function Definition and Calling

def greet():
    print("Hello, World!")

greet()


#------------------------------------------------------------------------------------
# Question 2: Function with Parameters

def personalized_greeting(name):
    print(f"Hello, {name}!")

personalized_greeting("Unako")


#------------------------------------------------------------------------------------
# Question 3: Function with Return Value

def square(number):
    return number * number

result = square(5)
print("Square:", result)


#------------------------------------------------------------------------------------
# Question 4: Function with Multiple Parameters and Return Value

def rectangle_area(length, width):
    return length * width

area = rectangle_area(4, 5)
print("Area:", area)


#------------------------------------------------------------------------------------
# Question 5: Using a Function as an Argument

def apply_operation(func, number):
    return func(number)

def double(number):
    return number * 2

print("Double result:", apply_operation(double, 7))
print("Square result:", apply_operation(square, 3))