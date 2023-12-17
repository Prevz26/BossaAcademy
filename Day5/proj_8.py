names = ['precious', 'ojogu']
vowels = 'a,e,i,o,u'

for name in names:
    if name[0] in vowels:
        print(f"{name} starts with a vowel.")
    else:
        print(f"{name} does not start with a vowel.")