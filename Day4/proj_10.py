def multiplication_table(user_input):
    if user_input.isdigit():
        user_input = int(user_input)
    else:
        print('Enter a valid number')

    for num in range(0, 12):
        print (user_input * num)
   
user_input = input('enter a value')
multiplication_table(user_input)
    