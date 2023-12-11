def vowel_counter(user_input):
    counter = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in user_input:
        if char in vowels:
            counter += 1
            print (f'There are {counter} vowel in {user_input}: {char}')
            
user_input = input("Enter something: ")
vowel_counter(user_input)
        