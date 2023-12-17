def word_counter(user_input):
    if isinstance(user_input, str):
        word = user_input.split()
    length_word = len(word)
    return (length_word)
word = input('Enter a word')

print(f"they are {word_counter(word)} words in {word}")