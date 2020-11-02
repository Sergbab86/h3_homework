
password = '213343dr56'


def validate_password(password):
    letters_list = []
    numbers_list = []
    letters_list = [letters_list.append for i in password if i.isalpha()]
    numbers_list = [numbers_list.append for i in password if i.isdigit()]
    if not password.isalnum():
        print('Строка содержит запрещенные символы')
    elif len(letters_list) % 2 != 0:
        print('Содержит нечетное количество букв')
    elif len(numbers_list) % 2 == 0:
        print('Содержит четное количество цифр')


def _validate_symbols(password):
    if not password.isalnum():
        return False
    return True


def _validate_letters_even(password):
    letters_list = []
    letters_list = [letters_list.append for i in password if i.isalpha()]
    if len(letters_list) % 2 != 0:
        return False
    return True


def _validate_numbers_odd(password):
    numbers_list = []
    numbers_list = [numbers_list.append for i in password if i.isdigit()]
    if len(numbers_list) % 2 == 0:
        return False
    return True


print(validate_password(password))
