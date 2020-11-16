import os















def log_reading(func):
    def wrapper(*args):
        directory = '/Users/julia/Downloads'
        file_list = os.listdir(directory)
        log_files = list(filter(lambda x: x.endswith('.log'), file_list))
        print(log_files)
    return wrapper


@log_reading
def get_files():
    directory = '/Users/julia/Downloads'
    file_list = os.listdir(directory)
    return file_list


print(get_files())
