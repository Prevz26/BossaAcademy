def new_list():
    number = [20, 40, 33, 45, 60]
    new_list = []
    for num in number:
        if num % 2 == 0:
            new_list.append(num)

    print(new_list)

new_list()
