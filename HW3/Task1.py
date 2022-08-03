# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

lst_lenght = int(input("Введите количество строк для создания списка: "))
lst = [input(f"Введие {i+1} строку: ") for i in range(lst_lenght)]
number = input("Введите число для поиска: ")
determ = False
for i in lst:
    if number in i:
        determ = True
        break
print("Число есть в списке" if determ else "Число в списке отсутствует")