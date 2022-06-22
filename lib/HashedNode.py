import hashlib

class HashedNode:
    """
    An implementation of a Merkle Node using sha256 hashing.
    Values are utf-8 forced before hashing.
    
    Attributes are self explanatory


    Construction and creation of merkle trees can be found on the utils.py file
    """
    def __init__(self, input_value) -> None:
        self.left_leave = None
        self.right_leave = None
        self.input_value = input_value
        self.hashed_value = hashlib.sha256(input_value.encode("utf-8")).hexdigest()

    def __repr__(self) -> str:
        return "left leave: " + str(self.left_leave) + "right leave: " + str(self.right_leave) \
             + "Hash: " + str(self.hashed_value) + "Input Value:" + self.input_value

    def __str__(self) -> str:
        return str(self.left_leave) + str(self.right_leave) + str(self.input_value) + str(self.hashed_value) 
    
