def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = ""
    for char in input_string:
        if char not in vowels:
            result += char
    return result

original_string = input('Enter something')
modified_string = remove_vowels(original_string)

print("Original String:", original_string)
print("Modified String without vowels:", modified_string)
