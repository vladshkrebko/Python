def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


def checkNumber(num):
    if 6 <= num <= 7:
        print("Выходной день")
    elif 0 < num < 6:
        print("Рабочий день")
    else:
        print("Дней недели всего 7")


num = InputNumbers("Введите номер дня недели от 1 до 7: ")
checkNumber(num)