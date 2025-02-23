def names(first_name, last_name):
    if (first_name == "Rishi"):
        print("correct")
    else:
        print("incorrect")
names("Rishi","Vishal")        

def age(age = 29, life = 100, name = "rishi"):
    if (name == "rishi"):
        print(life - age)
    else:
        print("incorrect")
age()        
#user defined function
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
#function parameters
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3) 
print(result)

#global variable
x = "Rishi"

def modify_global():
    global x
    x = "Vishal"

modify_global()
print(x)  # Output: 20

#lamda function
def square(x):
    print(x**2)
square(5)

square = lambda x: x ** 2
print(square(5))

#anonymous function
## Create a list of numbers
numbers = [3, -7, 2, 9, -1, 4, 8, -6, 5]

# Using len() to get the length of the list
list_length = len(numbers)
print(f"The list contains {list_length} numbers.")

# Using sum() to calculate the sum of all numbers
total_sum = sum(numbers)
print(f"The sum of all numbers is: {total_sum}")

# Using max() and min() to find the highest and lowest numbers
highest = max(numbers)
lowest = min(numbers)
print(f"The highest number is {highest} and the lowest is {lowest}.")

# Using sorted() to sort the list
sorted_numbers = sorted(numbers)
print(f"The sorted list is: {sorted_numbers}")

# Using abs() with map() to get absolute values
absolute_values = list(map(abs, numbers))
print(f"The absolute values are: {absolute_values}")

# Using filter() to get only positive numbers
positive_numbers = list(filter(lambda x: x > 0, numbers))
print(f"The positive numbers are: {positive_numbers}")

# Using round() to round the average to 2 decimal places
average = round(sum(numbers) / len(numbers), 2)
print(f"The average of the numbers is: {average}")

# Using type() to check the data type of a variable
print(f"The type of 'numbers' is: {type(numbers)}")

# Using str() to convert a number to a string
string_number = str(total_sum)
print(f"The sum as a string is '{string_number}' and its type is {type(string_number)}")