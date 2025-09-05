"""
Create a Python program:

The program asks the user for input N (positive integer) and reads it.

Then the program asks the user to provide N (x, y) pairs (one by one) and reads all of them:
    first: x value, then: y value for every pair one by one.
        X is treated as the input feature and Y is treated as the class label.
        X is a real number, Y is a non-negative integer.

This set of pairs constitutes the training set TrainS = {(x, y)_i}, i = 1..N.

Then the program asks the user for input M (positive integer) and reads it.

Then the program asks the user to provide M (x, y) pairs (one by one) and reads all of them:
    first: x value, then: y value for every pair one by one.
        X is treated as the input feature and Y is treated as the class label.
        X is a real number, Y is a non-negative integer.

This set of pairs constitutes the test set TestS = {(x, y)_i}, i = 1..M.

In the end, the program outputs:
    the best k for the kNN Classification method and
    the corresponding test accuracy.
    kNN Classifier should be trained on pairs from TrainS,
        tested on x values from TestS and
        compared with y values from TestS.

The basic functionality of data processing (data initialization, data insertion), should be done using Numpy library while
    the computation (ML) part should be done using Scikit-learn library as much as possible
    (note: you can combine with what you've done from the previous tasks).

Note: you can try the following range of k: 1 <= k <= 10.
"""

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from util import *


def prompt_for_set(prompt=''):
    # prompts for input N (positive integer)
    size = get_a_number(prompt, lambda x: x > 0 and x.is_integer(),
                     "Expecting a provide positive integer")
    if size is None:
        return
    size = int(size)

    points = np.empty((size, 2))
    ind = 0

    # prompts for N points (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one.
    for i in range(1, size + 1):
        # X is a real number, Y is a non-negative integer.
        print(f"Point {i:d}:")
        X = get_a_number("\tX: ")
        if X is None:
            return
        Y = get_a_number("\tY: ", lambda x: x >= 0 and x.is_integer(), "Expecting a non-negative integer")
        if Y is None:
            return
        print(f"\tPoint {i:d} = ({print_value(X)}, {print_value(Y)})")

        points[ind] = X, Y
        ind += 1
    return points

def simple_python_program():
    training_set = prompt_for_set("Please provide Training Set Size N as a positive integer: ")
    test_set = prompt_for_set("Please provide Test Set Size M as a positive integer: ")

    """
    In the end, the program outputs:
        the best k for the kNN Classification method and
        the corresponding test accuracy.
        kNN Classifier should be trained on pairs from TrainS,
            tested on x values from TestS and
            compared with y values from TestS.
    Note: you can try the following range of k: 1 <= k <= 10.
    """

    print("Scoring...")

    ks = np.arange(1, 1 + min(10, len(training_set)))
    accuracy = np.zeros(len(ks))
    for i, k in enumerate(ks):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(training_set[:, :1], training_set[:, 1])
        accuracy[i] = knn.score(test_set[:, :1], test_set[:, 1] )

    highest_accuracy_ind = np.argmax(accuracy)
    highest_k = ks[highest_accuracy_ind]
    highest_accuracy = accuracy[highest_accuracy_ind]

    print("Scores:")
    for k, acc in zip(ks, accuracy):
        print(f"\tk = {k:d}, accuracy = {acc:f}")
    print("Highest score:")
    print(f"\tFor k = {highest_k:d}, accuracy = {highest_accuracy:f}")

if __name__ == "__main__":
    simple_python_program()