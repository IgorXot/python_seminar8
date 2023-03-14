def printAll():
    print('\n'*100)
    data = open('file.txt', 'r')
    for line in data:
        print(line)
    data.close()
    print('\n')