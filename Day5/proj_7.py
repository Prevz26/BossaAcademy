def reverse_sentence(sentence):
    if isinstance(sentence, str):
        words = sentence.split()
        reversed_sentence = ' '.join(reversed(words))
        return reversed_sentence
    else:
        return "Input is not a valid string."

user_input = input('Enter a sentence: ')
result = reverse_sentence(user_input)
print(f"The reversed sentence is: {result}")
