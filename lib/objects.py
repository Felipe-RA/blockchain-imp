import hashlib

class HashedNode:
    def __init__(self, input_value) -> object:
        self.left_leave = None
        self.right_leave = None
        self.input_value = input_value
        self.hashed_value = hashlib.sha256(input_value.encode("utf-8")).hexdigest()

