def is_even(user_input):
    if user_input % 2 == 0:
        return True
    elif user_input % 2 != 0:
        return False

while True:
    number = input("enter a number")
    if number.isdigit():
        number = int(number)
        if is_even(number):
            print(f"{number} is even")
            break
        else:
            print(f"{number} is odd")
            break
    else:
        print('Enter a valid Number')
        continue
    