"""
Create a Python program:

The program asks the user for input N (positive integer) and reads it.

Then the program asks the user to provide N (x, y) points (one by one) and reads all of them:
    first: x value, then: y value for every point one by one.
    X is treated as the ground truth (correct) class label and Y is treated as the predicted class.
    Both X and Y are either 0 or 1.

In the end, the program outputs: the Precision and Recall based on the inputs.

The basic functionality of data processing (data initialization, data insertion), should be done using Numpy library
    while the computation (ML) part should be done using Scikit-learn library as much as possible
    (note: you can combine with what you've done from the previous tasks).
"""

import numpy as np
from sklearn.metrics import precision_score, recall_score
from util import *


class module8_oop:
    def __init__(self, N):
        if not isinstance(N, int) or N < 1:
            raise ValueError("N must be a positive integer")
        self.N = N
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

    def score(self):
        precision = precision_score(self.points[:,0], self.points[:,1], average='binary')
        recall = recall_score(self.points[:,0], self.points[:,1], average='binary')
        return precision, recall


def simple_python_program():
    # prompts for input N (positive integer)
    N = get_a_number("Please provide positive integer N: ", lambda x: x > 0 and x.is_integer())
    if N is None:
        return
    N = int(N)

    my_points = module8_oop(N)

    def check_input(x):
        ret = x in (0, 1)
        if not ret:
            print("Please provide 0 or 1")
        return ret

    # prompts for N points (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one.
    for i in range(1, N+1):
        print(f"Point {i:d}:")
        x = get_a_number("\tx: ", check_input)
        if x is None:
            return
        y = get_a_number("\ty: ", check_input)
        if y is None:
            return

        my_points.add_point(x, y)
        print(f"\tPoint {i:d} = ({print_value(x)}, {print_value(y)})")

    Precision_Score, Recall_Score = my_points.score()
    print("Scoring...")
    print(f"\t{Precision_Score=}")
    print(f"\t{Recall_Score=}")

if __name__ == "__main__":
    simple_python_program()
