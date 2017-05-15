class Pseudohex():
    def __init__(self, value=0):
        self.valid = '0123456789ABCDEFGHJKLMNPQRSTUVWXYZ'
        if isinstance(value, str):
            if self.valid.find(value) != -1:
                self._value = self.valid.find(value)
            else:
                raise ValueError('Invalid value {}'.format(value))
        elif isinstance(value, int):
            if value < len(self.valid) and value >= 0:
                self._value = value
            else:
                raise ValueError('Invalid value {}'.format(value))
        else:
            raise TypeError(
                '%s %s should be int or str', type(value), value)

    def __int__(self):
        return self._value

    def __index__(self):
        return self.__int__()

    def __str__(self):
        return self.valid[self._value]

    def __cmp__(self, other):
        if isinstance(other, str):
            if self.valid[self._value] < other:
                return -1
            elif self.valid[self._value] == other:
                return 0
            elif self.valid[self._value] > other:
                return 1
        elif isinstance(other, int):
            if self._value < other:
                return -1
            elif self._value == other:
                return 0
            elif self._value > other:
                return 1
