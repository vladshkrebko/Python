# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
S = input("Введите текст: ")

def coding(text):
    count = 1
    Alp = ''
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            Alp = Alp + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text)-2] != text[-1]):
            Alp = Alp + str(count) + text[-1]
    return Alp

def decoding(tekst):
    number = ''
    Alp = ''
    for i in range(len(tekst)):
        if not tekst[i].isalpha():
            number += tekst[i]
        else:
            Alp = Alp + tekst[i] * int(number)
            number = ''
    return Alp

print(f"Кодирование: {coding(S)}")
print(f"Декодирование: {decoding(coding(S))}")