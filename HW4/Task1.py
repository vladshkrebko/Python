# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def Search(num):
    rezult = []

    for i in range(2, num):
        if num % i == 0:
            num /= i
            rezult.append(i)
    return rezult

def Input(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Неверный ввод, введите число.")
    return number
num = Input("Задайте натуральное число N: \n")

print(f"Список множителей числа {num} :\n{Search(num)}")