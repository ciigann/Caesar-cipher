from colorama import Style

index = 0
while index != 1 and index != 2:  # проверка корректности ввода запросса
    try:
        index = int(input('Выберите: 1 - закодировать сообщение, 2 - раскодировать сообщение\n'))
        if index != 1 and index != 2:  # если пользователь ввел числа не 1 и 2
            print('\033[31m', 'Такого варианта ответа нет!!!' + Style.RESET_ALL)
    except ValueError:  # Если пользователь ввел буквенные символы
        print('\033[31m', 'Вариант ответа должен быть задан числом: 1 или 2!!!' + Style.RESET_ALL)
        pass
if index == 2:  # если 2 - раскодировать сообщение, то
    index = -1  # прировняли множитель к -1 чтобы сдвиг пошел в обратную сторону

string = input('Введите строку c сообщением: ')

shift = 0  # шаг сдвига
while shift == 0:
    try:  # что бы проверить является ли введенная строка числом попробуем преобразовать ее в int и будем ловить исключение
        shift = int(input('Введите шаг сдвига: '))
    except ValueError:
        shift = 0
        print('\033[31m', 'Введенный шаг сдвига должен быть задан целым числом !!!' + Style.RESET_ALL)
        pass

ABC_big = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'  # алфавит с заглавнями буквами
ABC_smale = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'  # алфавит со строчными буквами
new_string = ''  # закодированная строка

for i in range(0, len(string)):
    if string[i] in ABC_big:  # проверяем является ли символ заглавной буквой
        key = ABC_big.find(str(string[i]))
        new_key = (key + shift * index) % 33  # кодируем заглавную букву
        new_string += ABC_big[new_key]  # добавить заглавную букву в новую строку
    elif string[i] in ABC_smale:  # проверяем является ли символ строчной буквой
        key = ABC_smale.find(str(string[i]))
        new_key = (key + shift * index) % 33  # кодируем строчную букву
        new_string += ABC_smale[new_key]  # добавить строчную букву в новую строку
    else:  # символы которые не кодируются
        new_string += string[i] # добавить символ в новую строку
if index == 1:
    print('Закодированное сообщение: ', new_string)
else:
    print('Раскодированное сообщение: ', new_string)
