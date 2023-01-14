def ivsj():
    file = open("task.10.txt","r")
    data = file.read()
    for letter in data:
        if letter == 'J':
            print("I", end="")
        else:
            print(letter,end="")

    file.close()

ivsj()