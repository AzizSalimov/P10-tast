def a_vs_m():
    file = open('task.10,txt','r')
    data = file.read()
    counta=0
    countm=0
    for letter in data:
        if letter == 'A' or letter =='a':
            counta += 1
        elif letter == 'M' or letter =='m':
            countm += 1

    file.close()
    print('A and a:',counta)
    print('M and m:',countm)

a_vs_m()