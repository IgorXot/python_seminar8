from show_data import *
from find_data import *
from change import *
from delite import *

def menuHello():
    print("1.Добавить")
    print("2.Вывести всех")
    print("3.Поиск по фамилии")
    print("4.Внести изменения")
    print("5.Удалить данные")
    print("6.Выход")
    userInput = int(input())
    if userInput == 1:
        addData()
        return True
    if userInput == 2:
        printAll()
        return True
    if userInput == 3:
        find(input("Введите фамилию: "))
        return True
    if userInput == 4:
        find(input("Введите что нужно изменить: "), input("Введите измененные данные: "))
        return True
    if userInput == 5:
        find(input("Введите удаляемое имя: "))
        return True
    if userInput == 6:
        return False

def addData():
    data = open('file.txt', 'a')
    print('\n'*100) 
    first_name = input("Введите имя: ")
    second_name = input("Введите фамилию: ")
    mid_name = input("Введите отчество: ")
    number = input("Введите номер телефона")
    item = [first_name, second_name, mid_name, number]
    s = ' '
    data.writelines(s.join(item) + '\n')
    data.close()
    print('\n'*100)

