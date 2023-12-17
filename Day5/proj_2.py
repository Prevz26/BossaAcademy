def reverse_string(user_input):
    reverse = ''
    for char in user_input:
        reverse = char + reverse
    print(reverse)
user_input = input('Enter a word')
reverse_string(user_input)