user_input = input('enter a sentence: ')
if isinstance(user_input, str):
    split_input = list (user_input.split())  
    max_length = len(split_input[0])
    max_word = split_input[0]
    
    for word in split_input:
        if len(word) > max_length:
            max_length = len(word)
            max_word = word
    print ( f"The word with the max letter is {max_word} with a length of {max_length}")
  

