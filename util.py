def get_a_number(prompt='', check=None):
    while True:
        try:
            tmp = input(prompt)
            tmp = float(tmp)
        except ValueError as e:
            print(e)
            continue
        except EOFError:
            return None, None

        if check is None or check(tmp):
            return tmp


def print_value(x):
    return int(x) if x.is_integer() else x
