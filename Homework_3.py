
url_list = ['/catalog/ldjfn', 'dlfjhg', '/catalog/12334', '/catalog/9999']


# 1 часть(не знаю как делать)
def catalog_finder(url_list):
    for _ in url_list:
        result_list = []
        result_list.join.
        print(result_list)


# 2 часть
def get_str_center(input_str):
    output_str = None
    if len(input_str) % 2 == 0:
        output_str = input_str[len(input_str) // 2:(len(input_str) // 2) + 2]
    else:
        output_str = input_str[len(input_str) // 2:(len(input_str) // 2) + 3]
    return output_str


# 3 часть
def count_symbols(input_str):
    output_dict = {}
    for i in set(input_str):
        output_dict[i] = input_str.count(i)
    return output_dict


# 4 часть
def mix_strings(str1, str2):
    result_str = str1[:len(str1) // 2] + str2 + str1[(len(str1) // 2) + 1:]
    return result_str


# 5 часть
def even_int_generator():
    lst1 = [i for i in range(101)]
    lst2 = [i for i in lst1 if i % 2 == 0]
