def display_message(load):
    with open(load, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')

display_message('第五章.txt')