def remove_duplicates(input_string):
    if isinstance(input_string, str):
        unique_chars = set()
        result = []

        for char in input_string:
            if char not in unique_chars:
                result.append(char)
                unique_chars.add(char)

        return ''.join(result)
    else:
        return "Input is not a valid string."

# Example usage:
user_input = input('Enter a string: ')
result = remove_duplicates(user_input)
print(f"The string without duplicates is: {result}")
