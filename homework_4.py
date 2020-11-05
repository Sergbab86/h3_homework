
password = 'g786^&r'


def _validate_symbols(password):
    return password.isalnum()


def _validate_letters_even(password):
    letters_list = [i for i in password if i.isalpha()]
    return not len(letters_list) % 2


def _validate_numbers_odd(password):
    numbers_list = [i for i in password if i.isdigit()]
    return len(numbers_list) % 2 == 0


def validate_password(password):
    if _validate_symbols:
        print('Строка содержит запрещенные символы')
        return False
    elif _validate_letters_even:
        print('Содержит нечетное количество букв')
    elif not _validate_numbers_odd:
        print('Содержит четное количество цифр')



print(validate_password(password))
