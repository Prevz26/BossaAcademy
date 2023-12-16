user_input = input('Enter a number: ')
new_list = list(user_input)

digit_sum = 0
for num in new_list:
    if num.isdigit():
        num = int(num)
        digit_sum += num
    else:
        print("enter a valid number")
    print(f"Sum of the digits: {digit_sum}" )
