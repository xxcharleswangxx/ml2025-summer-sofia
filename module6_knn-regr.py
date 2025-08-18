"""
Create a Python program:

The program asks the user for input N (positive integer) and reads it.

Then the program asks the user for input k (positive integer) and reads it.

Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one. X and Y are the real numbers.

In the end, the program asks the user for input X and outputs: the result (Y) of k-NN Regression if k <= N, or any error message otherwise.

The basic functionality of data processing (data initialization, data insertion, data calculation) should be done using Numpy library as much as possible (note: you can combine with OOP from the previous task).
"""

import numpy as np


class module6_oop:
    def __init__(self, N, k):
        if not isinstance(N, int) or N < 1:
            raise ValueError("N must be a positive integer")
        if not isinstance(k, int) or k < 1:
            raise ValueError("k must be a positive integer")
        self.N = N
        self.k = k
        self.points = np.empty((N, 2))
        self.ind = 0

    def add_point(self, x, y):
        if not isinstance(x, (int, float)):
            raise ValueError(f"x must be a number, got {type(x)}")
        if not isinstance(y, (int, float)):
            raise ValueError(f"y must be a number, got {type(x)}")
        if self.ind >= self.N:
            raise ValueError("Too many points")
        self.points[self.ind] = x, y
        self.ind += 1

    def predict(self, x):
        if not isinstance(x, (int, float)):
            raise ValueError(f"x must be a number, got {type(x)}")
        # L1 distance from all points
        dis = np.abs(self.points[:, 0] - x)
        # sort distances and get mean of k sorted labels
        ind = np.argsort(dis)
        ys = np.take_along_axis(self.points[:,1], ind, axis=0)
        return ys[:self.k].mean()


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

    # prompts for input k (positive integer)
    k = get_a_number("Please provide positive integer k: ", lambda x: x > 0 and x.is_integer())
    if k is None:
        return
    k = int(k)
    my_points = module6_oop(N, k)

    # prompts for N points (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one.
    for i in range(1, N+1):
        x = get_a_number(f"Please provide point {i:d}:\n")
        if x is None:
            return
        y = get_a_number()
        if y is None:
            return

        my_points.add_point(x, y)
        print(f"\tgot ({print_value(x)}, {print_value(y)})")

    # prompts for input X (integer) and outputs:
    #   the result (Y) of k-NN Regression if k <= N
    #   or any error message otherwise
    X = get_a_number("Please provide a number X: ")
    if X is None:
        return

    if k > N:
        raise ValueError("k must be <= N")

    Y = my_points.predict(X)
    print(f"For X={print_value(X)}, predicated Y={print_value(Y)}")

if __name__ == "__main__":
    simple_python_program()
