import pickle


def add_record():
    file = open("employee.dat", "ab")
    emp = {}
    emp['empcode'] = int(input("Enter employee code: "))
    emp['name'] = input("Enter employee Name: ")
    emp['salary'] = int(input("Enter salary: "))
    pickle.dump(emp, file)
    file.close()


def search():
    file = open("employee.dat", "rb")
    try:
        while True:
            emp = pickle.load(file)
            if emp['salary'] > 30000:
                print(emp)
    except EOFError:
        pass
    file.close()


# To test working of functions
def testProgram():
    while True:
        add_record()
        choice = input("Add more record (y/n)? ")
        if choice in 'Nn':
            break
    print('Employee details having salary more than 30000')
    search()


testProgram()