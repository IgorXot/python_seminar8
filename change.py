def Change(data, redata):
    with open('file.txt', 'r', encoding='utf-8') as f:
        old_data = f.read()
    new_data = old_data.replace(data,redata)
    with open('file.txt', 'w', encoding='utf-8') as f:
        f.write(new_data)
    print('Изменения внесены\n')