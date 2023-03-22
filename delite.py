def Delite(data):
    with open('file.txt', enconding='utf-8') as infile, open('file1.txt', "w", enconding='utf-8') as outfile:
        for line in infile:
            if data.lower() not in line.lower():
                outfile.write(line)
    import os
    os.remove('file.txt')
    os.rename('file.txt', 'file1.txt')
    print('\удалено')