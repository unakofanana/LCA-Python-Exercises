# Question 1: Creating and Modifying Lists

fruits = ["apple", "banana", "orange"]

# Add a fruit to the end
fruits.append("grape")

# Insert a fruit at the beginning
fruits.insert(0, "mango")

# Remove a fruit
fruits.remove("banana")

print("Modified fruits list:", fruits)


#-------------------------------------------------------------------------
# Question 2: List Operations

numbers = [1, 2, 3, 4, 5]

# Create squared list
squares = [num * num for num in numbers]

# Sum and average
total = sum(numbers)
average = total / len(numbers)

print("Numbers:", numbers)
print("Squares:", squares)
print("Sum:", total)
print("Average:", average)


#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

countries = {
    "South Africa": "Pretoria",
    "France": "Paris",
    "Japan": "Tokyo"
}

# Add new country
countries["Germany"] = "Berlin"

# Update existing capital
countries["France"] = "Paris (Updated)"

# Remove a country
countries.pop("Japan")

print("Modified countries dictionary:", countries)


#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple"
}

# Print keys
print("Fruits:", fruit_colors.keys())

# Print values
print("Colors:", fruit_colors.values())

# Print each pair
for fruit, color in fruit_colors.items():
    print(fruit, "is", color)

# Check if fruit exists
check_fruit = "apple"

if check_fruit in fruit_colors:
    print(check_fruit, "is", fruit_colors[check_fruit])
else:
    print(check_fruit, "not found")