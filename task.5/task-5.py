def enumerator():
    file = open("task.5.txt","r")
    data = file.read()
    words = data.split()
    count = 0
    for word in words:
        if len(f"{word}") <= 4:
            count += word
            print(count)


    file.close()

enumerator()