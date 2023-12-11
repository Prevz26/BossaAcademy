user_input = int(input("enter something"))
one_hour = 60

if user_input % one_hour == 0:
    print(user_input / one_hour)
elif user_input % 60 != 0:
    print(user_input % 60)
