sentence_input = input("enter a sentence: ")
word_input = input("enter a word: ")

for word in sentence_input:
    if word == word_input:
        print(f"{word_input} is in the sentence.")
    else:
        print(f"{word_input} is not in the sentence.")

