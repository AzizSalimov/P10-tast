import pickle


def countRec(country):
    infile = open("game.dat","rb")
    outfile = open("basket.dat","wb")

    try:
        while True:
            record = pickle.load(infile)
            if record[0] == "Basket Ball":
                pickle.dump(record, outfile)
    except EOFError:
        pass
    infile.close()
    outfile.close()
