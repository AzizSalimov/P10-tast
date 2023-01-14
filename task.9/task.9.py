def count_hash():
    file = open("task.8.txt","r")
    data = file.read()
    for letter in data:
        print(letter, end="#")

    file.close()

count_hash()