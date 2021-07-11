from enum import Enum

class TTypes(Enum):
    NUMBER = 0
    STRING = 1
    COMMAND = 2

class Token:
    def __init__(self, value, _type, misc=None):
        self.value = value
        self.type = _type
        self.misc = misc

    def update(self, misc):
        self.misc = misc

    def __str__(self):
        val_str = repr(self.value)
        return f"Token({val_str}, {self.type}, {self.misc})"

