import os

# def str_to_html(tags):
#     def decorator(func):
#         tag_base = {
#             "italic": f"<i>%text%</i>",
#             "bold": f"<b>%text%</b>",
#             "underline": f"<u>%text%</u>",
#         }
#
#         # def wrapper(text):
#         # new_text =
#         # return wrapper
#     return decorator
#
#
# @str_to_html(["italic", "bold"])
# def get_text(text):
#     return text
#
#
# print(get_text())


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
