def reverse_string(user_input):
    reversed_string = ''
    for char in user_input:
        reversed_string = char + reversed_string
    print (reversed_string)

reverse_string("hello world")
