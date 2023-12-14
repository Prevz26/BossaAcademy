def is_prime(user_input):
    if user_input < 2:
        return False
    for i in range(2, int(user_input**0.5) + 1):
        if user_input % i == 0:
            return False
    return True

while True:
    user_input = input ("Enter a number: ")
    if user_input.isdigit():
        user_input = int(user_input)
    else:
        print("Enter a valid option")
        
    if is_prime(user_input):
        print("This is a prime number")
    else:
         print("This is not a prime number")
         
    choice = input("Do you wish to continue:")
    if choice == "yes":
        continue
    elif choice == "no":
        exit()
    else:
        print("Enter a valid option")
prime(user_input)
