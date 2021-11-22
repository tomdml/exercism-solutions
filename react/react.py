class InputCell:
    def __init__(self, initial_value):
        self._value = initial_value
        self.callbacks = set()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value_in):
        self._value = value_in
        """
        old_vals = [cell.value for cell in self.callback_targets]
        self._value = value_in
        new_vals = [cell.value for cell in self.callback_targets]
        print(self._value)
        print(old_vals)
        print(new_vals)
        print(self.callback_targets)
        for old, new, target in zip(old_vals, new_vals, self.callback_targets):
            if old != new:
                for func in target.callback_funcs:
                    func(target.value)
        """


class ComputeCell:
    def __init__(self, target_cells, cells_func):
        self._target_cells = target_cells
        self._cells_func = cells_func
        self.callback_funcs = set()
        self.callback_targets = set()

    @property
    def value(self):
        return self._cells_func([cell.value for cell in self._target_cells])

    def add_callback(self, callback_func):
        print('in add_callback')
        print(callback_func)
        print(self._target_cells)
        for cell in self._target_cells:
            if isinstance(cell, InputCell):
                cell.callback_targets.add(self)
            else:
                print('idk what to do here')
        self.callback_funcs.add(callback_func)

    def remove_callback(self, callback_func):
        if callback_func in self.callback_funcs:
            self.callback_funcs.remove(callback_func)
