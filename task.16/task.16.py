import pickle


def total_fees():
    file = open("school.dat", "rb")
    try:
        total = 0
        while True:
            record = pickle.load(file)
            total += record[3]:
            except EOFError:
            pass
        print('Total Fees: ', total)
        file.close()
