string = input('Введите строку c сообщением: ')
shift = int(input('Введите шаг сдвига'))
ABC_big = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ABC_smale = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
new_string = ''

for i in range(0, len(string)):
    if string[i] in ABC_big:  # проверяем является ли символ заглавной буквой
        key = ABC_big.find(str(string[i]))
        new_key = (key + shift) % 33
        new_string += ABC_big[new_key]
    elif string[i] in ABC_smale:  # проверяем является ли символ строчной буквой
        key = ABC_smale.find(str(string[i]))
        new_key = (key + shift) % 33
        new_string += ABC_smale[new_key]
    else:
        new_string += string[i]
print('закодированная строка', new_string)
