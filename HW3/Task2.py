# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

def func(lst, find_str):
    if lst.count(find_str) > 1:
        k = lst.index(find_str)
        print(lst.index(find_str, k+len(find_str)))
    else:
        print(f"нет второго вхождения")

lst = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
f = "qwe"
func(lst, f)
lst = ["123", "234", 123, "567"]
f = "123"
func(lst, f)