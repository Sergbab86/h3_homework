
def do_cache(maxsize):
    def wrapper(a, b):
        storage = {f'{a},"*", {b}': a ** b}
        print(storage)



@do_cache(maxsize = 3)
def get_value(a, b):
  return a ** b


print(get_value(2, 3))
