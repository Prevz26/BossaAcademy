import string

def checker(user_input = "hello"):
    alphabet_set = set(string.ascii_lowercase)
    input_set = set(user_input.lower())
    return alphabet_set.issubset(input_set)

print(checker())