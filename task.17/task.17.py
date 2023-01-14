import pickle


def createFile():
    file = open("players.dat", "ab")
    Code = int(input("Enter player code: "))
    Name = input("Enter player Name: ")
    Country = input("Enter player country: ")
    Total_Runs = int(input("Enter total runs of player: "))
    record = [Code, Name, Country, Total_Runs]
    pickle.dump(record, file)
    file.close()


def search():
    file = open("players.dat", "rb")
    try:
        while True:
            record = pickle.load(file)
            if record[1][0] == 'A':
                print(record)
    except EOFError:
        pass
    file.close()


def countRec(Country):
    file = open("players.dat", "rb")
    count = 0
    try:
        while True:
            record = pickle.load(file)
            if record[2] == Country:
                count += 1
    except EOFError:
        pass
    return count
    file.close()


def testProgram():
    while True:
        createFile()
        choice = input("Add more record (y/n)? ")
        if choice in 'Nn':
            break
    print("the number of players whose name starts with A:", search())
    Country = input('Enter country name to search: ')
    n = countRec(Country)
    print("No of players are", n)


testProgram()
