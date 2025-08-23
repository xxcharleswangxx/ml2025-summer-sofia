"""
Create a Python program:

The program asks the user for input N (positive integer) and reads it.
Then the program asks the user for input k (positive integer) and reads it.
Then the program asks the user to provide N (x, y) points (one by one) and reads all of them:
    first: x value, then: y value for every point one by one. X and Y are the real numbers.

In the end, the program asks the user for input X and outputs:
    the result (Y) of k-NN Regression if k <= N, or any error message otherwise.
Additionally, provide the variance of labels in the training dataset.

The basic functionality of data processing (data initialization, data insertion), should be done using Numpy library
while the computation (ML) part should be done using Scikit-learn library as much as possible
(note: you can combine with what you've done from the previous task).
"""

import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from util import *

class module7_oop:
    def __init__(self, N, k):
        if not isinstance(N, int) or N < 1:
            raise ValueError("N must be a positive integer")
        if not isinstance(k, int) or k < 1:
            raise ValueError("k must be a positive integer")
        self.N = N
        self.k = k
        self.points = np.empty((N, 2))
        self.ind = 0
        self.knn = None

    def add_point(self, x, y):
        if not isinstance(x, (int, float)):
            raise ValueError(f"x must be a number, got {type(x)}")
        if not isinstance(y, (int, float)):
            raise ValueError(f"y must be a number, got {type(x)}")
        if self.ind >= self.N:
            raise ValueError("Too many points")
        self.points[self.ind] = x, y
        self.ind += 1
        self.knn = None

    def predict(self, x):
        if not isinstance(x, (int, float)):
            raise ValueError(f"x must be a number, got {type(x)}")

        if self.knn is None:
            self.knn = KNeighborsRegressor(n_neighbors=self.k)
            self.knn.fit(self.points[:, 0].reshape(-1, 1), self.points[:, 1])

        return self.knn.predict([[x]])[0], np.var(self.points[:, 1])


def simple_python_program():
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
    my_points = module7_oop(N, k)

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

    Y, var = my_points.predict(X)
    print(f"For X={print_value(X)}")
    print(f"predicated Y={print_value(Y)}")
    print(f"training label variance={var}")

if __name__ == "__main__":
    simple_python_program()
