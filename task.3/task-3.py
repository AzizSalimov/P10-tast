def get_info():
    line = open("task.txt", 'r')
    count = 0
    data = line.read()
    words = data.split()
    for word in words:
        count += 1
        print("Total words are:", count, word)
        line.close()


get_info()