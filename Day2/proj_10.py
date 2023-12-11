def prime(user_input)-> int:
    if user_input.isdigit():
        user_input = int(user_input)
    if user_input / user_input == 1 and user_input / 1 == user_input:
        print (f"{user_input} is a prime")
    else:
        print(f"{user_input} is not a prime")

user_input = input ("Enter a number: ")
prime(user_input)
