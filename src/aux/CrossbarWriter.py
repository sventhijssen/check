from core.BooleanFunction import BooleanFunction


class CrossbarWriter:

    def __init__(self, boolean_function: BooleanFunction, file_name: str):
        self.boolean_function = boolean_function
        self.file_name = file_name

    def write(self):
        with open(self.file_name, 'w') as f:
            f.write(self.boolean_function.write_xbar())
