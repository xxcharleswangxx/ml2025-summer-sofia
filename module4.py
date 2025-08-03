"""
3. Create a very simple python program:
    The program asks the user for input N (positive integer) and reads it
    
    Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
    
    In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, or the index (from 1 to N) of this X if the user inputed it before.
    
    Hint: use input() function
"""

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
    numbers = []
    for i in range(1, N+1):
        x = get_a_number(f"Please pro∂vide number {i:d}: ")
        if x is None:
            return
        numbers.append(x)
        print(f"\tgot {print_value(x)}")

    # prompts for input X (integer) and outputs:
    #   "-1" if there were no such X among N read numbers, or
    #   the index (from 1 to N) of this X if the user inputed it before
    X = get_a_number("Please provide a number X: ")
    if X is None:
        return
    try:
        ind = numbers.index(X) + 1
    except ValueError:
        ind = -1
    print(f"X = {print_value(X)} is at index {ind:d}")


if __name__ == "__main__":
    simple_python_program()
