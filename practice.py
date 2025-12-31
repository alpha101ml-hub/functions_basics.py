# 1. Define it
# def greet(name):
#     return f"hello, {name}!"

# message = greet("Alice")
# print(message)

'''
Scope: Why use def?

Variables created inside a def block are Local. They only exist while the function is running. This prevents your code from getting messy with too many global variables.
'''

# 1. We add a 'parameter' called f inside the parentheses
# def to_celsius(f):
#     return (f - 32) * 5/9

# # 2. Convert the input to a float so we can do math
# fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))

# # 3. Pass the input into the function
# result = to_celsius(fahrenheit_input)

# print(f"The temperature in Celsius is: {result}")

# def find_max(numbers):
#     my_max = 0
#     for n in numbers:
#         if n > my_max:
#             my_max = n
#     # Return is OUTSIDE the for-loop so it checks everything first
#     return my_max

# # Define the data
# my_list = [1, 2, 3, 4, 5]

# # Call the function and pass the list
# print(find_max(my_list))

# def filter_even(numbers):
#     even = []
#     for n in numbers:
#         if n % 2 == 0:
#             even.append(n)
#     return even

# print(filter_even([1,2,3,4,5,6,7,8,9]))

# def calculate_tip(bill_amount, tip):
#     tip_percentage = bill_amount*tip/ 100
#     return tip_percentage


# print(calculate_tip(50,20))

def evaluate_grade(score_list):
    results= {"Pass":0, "Fail":0}
    scores = []
    for score in score_list:
        if score >= 60:
            results["Pass"] += 1
        else:
            results["Fail"] += 1
            
    return results
        
print(evaluate_grade([85,42,76,90,55]))