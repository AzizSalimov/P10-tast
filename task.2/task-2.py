def number_of_rows():
    file = open('task.txt', 'r')
    count = 0
    for line in file:
        if line[0] not in 'T':
            count += 1
        file.close()
        print("Strings that do not start with the letter T", count)

    number_of_rows()