"""
1. Create a Python program:
    The program asks the user for input N (positive integer) and reads it

    Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)

    In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, or the index (from 1 to N) of this X if the user inputted it before.

    The basic functionality of data processing (data initialization, data insertion, data search) should be done via Object-Oriented Programming Paradigm (i.e. using Classes)
"""


class module5_oop:
    def __init__(self, N):
        if not isinstance(N, int) or N < 1:
            raise ValueError("N must be a positive integer")
        self.N = N
        self.numbers = []

    def add_number(self, x):
        if not isinstance(x, (int, float)):
            raise ValueError(f"x must be a number, got {type(x)}")
        self.numbers.append(x)

    def find_number(self, x):
        if not isinstance(x, (int, float)):
            raise ValueError(f"x must be a number, got {type(x)}")
        try:
            ind = self.numbers.index(x) + 1
        except ValueError:
            ind = -1
        return ind


def simple_python_program():
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

    # prompts for input N (positive integer)
    N = get_a_number("Please provide positive integer N: ", lambda x: x > 0 and x.is_integer())
    if N is None:
        return
    N = int(N)

    # prompts for N numbers (one by one) and reads all of them (again, one by one)
    my_numbers = module5_oop(N)
    for i in range(1, N + 1):
        x = get_a_number(f"Please pro∂vide number {i:d}: ")
        if x is None:
            return
        my_numbers.add_number(x)
        print(f"\tgot {print_value(x)}")

    # prompts for input X (integer) and outputs:
    #   "-1" if there were no such X among N read numbers, or
    #   the index (from 1 to N) of this X if the user inputed it before
    X = get_a_number("Please provide a number X: ")
    if X is None:
        return

    ind = my_numbers.find_number(X)
    print(f"X = {print_value(X)} is at index {ind:d}")

if __name__ == "__main__":
    simple_python_program()
