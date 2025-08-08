"""
2. Create the functionality outside of the main running code: i.e., create the module with the Class described in the item above, and name this module "module5_mod.py".
"""


class module5_mod:
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

