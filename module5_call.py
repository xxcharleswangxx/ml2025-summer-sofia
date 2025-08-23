"""
2. Create the main program "module5_call.py" that uses the Class description from the "*_mod" file.  Upload everything to the above-mentioned repo.
"""

from module5_mod import module5_mod
from util import *


def simple_python_program():
    # prompts for input N (positive integer)
    N = get_a_number("Please provide positive integer N: ", lambda x: x > 0 and x.is_integer())
    if N is None:
        return
    N = int(N)

    # prompts for N numbers (one by one) and reads all of them (again, one by one)
    my_numbers = module5_mod(N)
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
    return ind


if __name__ == "__main__":
    simple_python_program()
