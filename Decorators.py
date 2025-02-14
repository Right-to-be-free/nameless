#What Are Decorators in Python?
#Decorators in Python are a powerful design pattern that allows the modification of functions or methods without changing their actual code. 
# They are commonly used for logging, enforcing access control, instrumentation, caching, and more.

#A decorator is essentially a function that takes another function as an argument, adds some functionality, and returns a new function.



#Example 1: Basic Decorator

def new_func(func):
    def wrapper():
        func()
        print("my name is Rishi Vishal Garlapati")
        print("I am a student of JNAFU Hyderabad")
    return wrapper
    
@new_func
def my_func():
    print("Hello Everyone")

my_func()     


#example 2: Decorator with Arguments

def new_func(func):
    def wrapper(*arg, **kwargs):
        print(f"Function name is {func.__name__}")
        return func(*arg, **kwargs)
    return wrapper
@new_func
def add(a, b):
    return a + b
print(add(10, 20))

#Example 3: Decorator with Return Values
def Login_required(func):
        def wrapper(user_role):
            if user_role != "admin":
                print("Access denied")
                return
            return func(user_role)
        return wrapper
@Login_required
def view_admin_dashboard(user_role):
        print("Welcome to the admin dashboard!")

view_admin_dashboard("admin")  # Output: Welcome to the admin dashboard!
view_admin_dashboard("user")   # Output: Access denied

#Example 4: Decorator with Arguments and Return Values

import time

def time_it(func):
     def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
     return wrapper
@time_it
def calculate_sum(n):
     time.sleep(1)
     print("finished!")
calculate_sum(1000000)  # Output: Execution time: 1.000123456 seconds


    