def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

user_input = input("Enter a non-negative integer: ")
if user_input.isdigit():
    user_input = int(user_input)
    result = factorial(user_input)
    print(f"The factorial of {user_input} is: {result}")
else:
    print("Please enter a valid non-negative integer.")
