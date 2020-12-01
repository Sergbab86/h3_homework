from datetime import date

data = ({"first_name": "Guido", "last_name": "Van Rossum",
            "birth": date(1969, 6, 27), "email": "iamguido@python.org"},
            {"first_name": "Not Guido", "last_name": "But Van Rossum",
            "birth": date(1969, 6, 28), "email": "iamanoherguido@python.org"})


def _validate_input(data: tuple):
    first_name_len = 48
    last_name_len = 64
    max_age = 100
    for row in data:
        if not _validate_name(row['first_name'], first_name_len):
            return False
        if not _validate_name(row['last_name'], last_name_len):
            return False
        if not _validate_birth(row['birth'], max_age):
            return False
        if not _validate_email(row['email']):
            return False
    return True


def _validate_name(name, max_len):
    if not type(name) is str:
        return False
    if not 0 < len(name) < max_len:
        return False
    return True


def _validate_birth(birth, max_age):
    if not type(birth) is date:
        return False
    if birth > date.today():
        return False
    if date.today().year - birth.year > max_age:
        return False
    return True


def _validate_email(email):
    if not type(email) is str:
        return False
    email_parts = email.split('@')
    if len(email_parts) != 2:
        return False
    if not email_parts[0].isalnum():
        return False
    domain_parts = email_parts[1].split('.')
    if len(domain_parts) == 1:
        return False
    if not 2 <= len(domain_parts[-1]) <= 3:
        return False
    return True


def _format_output(data):



