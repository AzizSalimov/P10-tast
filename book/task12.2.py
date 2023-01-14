def counter_author(filepath, aouthor_name):
    counter = 0
    try:
        with open(filepath, 'r') as file:
            data = file.readlines()
    except FileNotFoundError as e:
        print(e)
    else:
        for line in data:
            for d in line.split(','):
                if d.split() == aouthor_name:
                    counter += 1
            return counter
    print(counter_author('Book.txt', 'AA'))